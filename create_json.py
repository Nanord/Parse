# -*- coding: utf-8 -*-

import json
import time


def create_json(element, url, header, title, start_time, len_content):
    # lists json
    lists = {}

    # url
    lists['url'] = url
    # header
    lists['header'] = header.replace('  ', ' ')
    # article
    lists['article'] = str(element.text)#.replace('\n\n', '\n')
    # img
    list_img = {}
    for img in element.find_all('img', src=True):
        img_text = img.text.replace('\n', '')
        img['src'] = img_text if img_text == '' else 'empty'
    lists['img'] = list_img
    # a
    list_a = {}
    for a in element.find_all('a', href=True):
        list_a[a['href']] = {'text': a.text.replace('\n', '')}
    lists['a'] = list_a
    # valuation
    if header.replace(' ', '') in title.replace(' ', ''):
        valuation = 2
    else:
        valuation = 1
    lists['valuation'] = valuation

    lists['time'] = time.time() - start_time

    lists['len_content'] = len_content
    # write to file
    y = json.dumps(lists, indent=4, ensure_ascii=False)
    return y
