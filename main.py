# coding=utf-8
import syss
from parse import parse


def main(url, flag_log=False):
    """
     list url
       url = [
       'https://habr.com/post/428988/',
       'https://vc.ru/life/51256-tilda-kak-i-skolko-mozhno-sekonomit-na-sozdanii-sayta?comment=959679',
       # 'https://nn.rbc.ru/nn/19/10/2018/5bc9f4d99a794773898f89e0',
       'https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html',
       # 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9_%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9F%D0%BE%D0%BC%D0%BF%D0%B5%D0%B8',
       # 'https://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python'
       ]
   """
    json = parse(url, flag_log)
    print(json)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "-p":
            main(sys.argv[2], False)
        elif sys.argv[1] == '-pl':
            main(sys.argv[1], True)
        else:
            sys.exit(1)
    else:
        main('https://habr.com/post/428988/', True)
