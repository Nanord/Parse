# -*- coding: utf-8 -*-

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
        res_css = requests.get(url=url_complete, timeout=20)
        if res_css.status_code != 200:
            res_css = requests.get(url=url_complete, timeout=20, header=rand_headers)
            if res_css.status_code != 200:
                return 1
        print(res_css.text)
