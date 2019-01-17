# -*- coding: utf-8 -*-
import codecs
import logging
import time

import requests
from bs4 import BeautifulSoup
from create_json import create_json
import random
from yaml import dump

from css_header import css_handler
from h1_header import h1_handler
from url_list import headers

def parse(page, flag_log):
    try:
        # headers
        # get text site
        rand_headers = random.choice(headers)

        res = requests.get(url=page, timeout=20)
        if res.status_code != 200:
            res = requests.get(url=page, timeout=20, header=rand_headers)
            if res.status_code != 200:
                return 1
        len_content = len(res.content)
        # START TIME
        start_time = time.time()
        # start parse
        soup = BeautifulSoup(res.text, 'html.parser')
        # extract this <script> and <style> tags
        for script in soup(["script", "style", "button"]):
            script.extract()
        # encode
        soup.decode('utf-8-sig')

        # title
        title = soup.find('title')

        header = soup.find('h1')
        element = None
        if header is not None:
            element = h1_handler(header)
        else:
            css_handler(soup)
            return 1
        if element is not None and header is not None:
            json = create_json(element, page, header.text.replace('\n', ''), title.text, start_time, len_content)
            if flag_log:
                # new File html
                file = open('logs/text.html', 'w')
                file.write("<head><meta charset=utf-8></head>")
                if element is not None:
                    file.write(str(element) + '<br><br>')
                file.close()
                file = codecs.open('logs/' + header.text.replace('\n', '').replace(' ', '_').replace('.', '') + '.json',
                                   'w', encoding="utf-8")
                file.write(str(json))
                file.close()
            end_tine = time.time() - start_time
            return json

        else:
            logging.error('Error: ' + page + ' page was not parsed')

    except Exception as err:
        pass
        #logging.critical(page + '_Error: ', err)
