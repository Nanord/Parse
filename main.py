# coding=utf-8
import sys
from parse import parse
import argparse


def main(url, flag_log=False):
    """
     list url
       url = [
        'https://habr.com/post/428988/',
        'https://vc.ru/life/51256-tilda-kak-i-skolko-mozhno-sekonomit-na-sozdanii-sayta?comment=959679',
        'https://nn.rbc.ru/nn/19/10/2018/5bc9f4d99a794773898f89e0',
        'https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html',
        'https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9_%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9F%D0%BE%D0%BC%D0%BF%D0%B5%D0%B8',
        'https://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python',
        'https://tass.ru/ekonomika/5896999?utm_source=yxnews&utm_medium=desktop',
        'https://www.vedomosti.ru/economics/news/2018/12/11/788956-mrot?utm_source=yxnews&utm_medium=desktop',
        'http://nsn.fm/hots/roskomnadzor-nakazhet-google.html?utm_source=yxnews&utm_medium=desktop',
        'https://1prime.ru/telecommunications_and_technologies/20181211/829528827.html?utm_source=yxnews&utm_medium=desktop',
        'https://echo.msk.ru/news/2331641-echo.html?utm_source=yxnews&utm_medium=desktop',
        'https://ura.news/news/1052363057?utm_source=yxnews&utm_medium=desktop',
        'https://www.mk.ru/politics/2018/12/11/v-germanii-nashli-sekretnoe-udostoverenie-lichnosti-shtazi-putina.html'
       ]
       13 sites
   """
    json = parse(url, flag_log)
    #print(json)

def create_parser_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help="Url")
    parser.add_argument('-r', type=str,choices=['json'],help="Report Json")
    return parser

if __name__ == '__main__':

    parser_arg = create_parser_arg()
    namespace = parser_arg.parse_args(sys.argv[1:])
    u = namespace.u
    rep_json = namespace.r

    if u is not None:
        if rep_json is not None:
            main(u, True)
        else: main (u, False)
    else:
        pass
    '''
    if len(sys.argv) > 1:
        if sys.argv[1] == "-p" and len(sys.argv) > 2:
            main(sys.argv[2], False)
        elif sys.argv[1] == '-pl' and len(sys.argv) > 2:
            main(sys.argv[2], True)
        else:
            sys.exit(1)
    else:
        main('https://www.mk.ru/politics/2018/12/11/v-germanii-nashli-sekretnoe-udostoverenie-lichnosti-shtazi-putina.html', True)
    '''