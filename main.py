# coding=utf-8
import locale
import sys
from parse import parse
import argparse

from url_list import url_list

def main(url, flag_log=False):
    json = parse(url, flag_log)
    return json


def print_example_sites():
#    print("Example url for you: ")
    for u in url_list:
        pass
 #       print(u)


def create_parser_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help="Url")
    parser.add_argument('-r', type=str, choices=['json'], help="Report Json")
    return parser


if __name__ == '__main__':
    parser_arg = create_parser_arg()
    namespace = parser_arg.parse_args(sys.argv[1:])
    u = namespace.u
    rep_json = namespace.r

    print_example_sites()

    if u is not None:
        if rep_json is not None:
            main(u, True)
        else:
            main(u, False)
    else:
        #url = str(input("Enter url: "))
        url = 'https://vc.ru/life/51256-tilda-kak-i-skolko-mozhno-sekonomit-na-sozdanii-sayta?comment=959679'
        main(url, True)
