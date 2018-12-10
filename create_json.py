import codecs
import json


def create_json(element, url, header):
    # lists json
    lists = {}

    # url
    lists['url'] = url
    # header
    lists['header'] = header.replace('  ', ' ')
    # article
    lists['article'] = str(element.text).replace('\n\n', '')
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
    # write to file
    y = json.dumps(lists, indent=4)
    #print(y)
    return y