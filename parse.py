import codecs
import logging

import requests
from bs4 import BeautifulSoup

from create_json import create_json

import random

headers = [
'User-Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
'User-Agent : Opera/7.54 (Windows NT 5.1; U) [en]',
'User-Agent : Mozilla/5.0 (Windows NT 5.0; U) Opera 7.21 [en]',
'User-Agent : Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.24'
]

def h1_handler(header):
    parent_el = header.parent
    print(parent_el)
    while True:
        if len(parent_el.text) > 1000:  # Add factors stoping //
            break
        else:
            parent_el = parent_el.parent
    return parent_el


def css_handler(soup):
    href_list = [] 
    stylesheet_list = ['stylesheet'] 
    link = soup.find_all('link')
    for l in link:
        if l.attrs['rel'] == stylesheet_list:
            href_list.append(l.attrs['href'])  

    for h in href_list:
        rand_headers = random.choice(headers)
        url_complete = 'https:' + h 
        res_css = requests.get(url= url_complete, timeout=20)
        if res_css.status_code != 200:
            res_css = requests.get(url=url_complete, timeout=20 ,header = rand_headers) 
            if res_css.status_code != 200:
                return 1
        print (res_css.text)
            

def parse(page, flag_log):
    try:
        # headers
        # get text site
        rand_headers = random.choice(headers)

        res = requests.get(url=page, timeout=20)
        if res.status_code != 200:
            res = requests.get(url=page, timeout=20 ,header = rand_headers) 
            if res.status_code != 200:
                return 1
        # start parse
        soup = BeautifulSoup(res.text, 'html.parser')
        # extract this <script> and <style> tags
        for script in soup(["script", "style", "button"]):
            script.extract()
        # encode
        soup.encode('UTF-8')

        header = soup.find('h1')
        element = None
        if header is not None:
            element = h1_handler(header)
        else:
            css_handler(soup)
            return 1
        if element is not None and header is not None:
            json = create_json(element, page, header.text.replace('\n', ''))
            if flag_log:
                # new File html
                file = open('logs/text.html', 'w')
                file.write("<head><meta charset=utf-8></head>")
                if element is not None:
                    file.write(str(element) + '<br><br>')
                file.close()
                file = codecs.open('logs/' + header.text.replace('\n', '').replace(' ', '_').replace('.', '') + '.json', 'w', 'utf-8')
                file.write(json)
                file.close()
            return json

        else:
            logging.error('Error: ' + page + ' page was not parsed')

    except Exception as err:
        logging.critical(page + '_Error: ', err)
