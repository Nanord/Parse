import json
import logging
import random
import sys

from parse import parse
import argparse

import time
from collections import OrderedDict

from main import main
from tests.average import average_arithmetic, average_gemetric, percentage
from tests.graphics import lineplot, lineplot2
from url_list import url_list


def generator_url(list_):
    if list_ is not None or len(list_) > 1:
        for j in range(0, len(list_)):
            u = random.choice(list_)
            if 'http' in u:
                url_list.append(u)


def test(generator=False):
    i = 0
    valuation_list = []
    time_list = []
    count_symbol_article_list = []
    metic_count_symbol_time = {}
    for url in url_list:
        if i > 10:
            break
        try:
            start_time = time.time()
            json_site = main(url, False)
            end_time = time.time() - start_time

            if json_site != '' and type(json_site) == str:
                json_site = json.loads(json_site)
                # end_time = float(json_site['time'])
                t = round(float(end_time), 2)
                if t < 2:
                    if json_site != 1:
                        time_list.append(t)
                        if int(json_site['valuation']) == 2:
                            # Метрика зависимости времени от кол-ва символов
                            metic_count_symbol_time[int(json_site['len_content'])] = t
                            # count_symbol_article_list.append(len(str(json_site['article'])))

                # Оценка парсига
                valuation_list.append(json_site['valuation'])
                a_list = [key for key in json_site['a'].keys()]
                # !!!
                if generator:
                    generator_url(a_list)
            else:
                if json_site == 1:
                    valuation_list.append(0.5)
                else:
                    valuation_list.append(0)
        except Exception as err:
            # time_list.append(0)
            # valuation_list.append(0)
            logging.critical('_Error: ', err)

        print(i)
        i += 1
    print(len(url_list))
    lineplot(x_data=[i for i in range(1, len(time_list) + 1)], y_data=time_list, x_label='site(count)',
             y_label='time(sec)',
             name='time')
    lineplot2(x_data=[i for i in range(1, len(valuation_list) + 1)], y_data=valuation_list, x_label='site(count)',
              y_label='valuation', name='valuation')

    sort = {}
    for k in sorted(metic_count_symbol_time.keys()):
        if metic_count_symbol_time[k] > 0.05:
            sort[k] = metic_count_symbol_time[k]

    lineplot(x_data=sort.keys(), y_data=sort.values(), x_label='count symbol', y_label='time(sec)',
             name='metic_count_symbol_time')

    # Средние значения
    sa = average_arithmetic(time_list)
    sg = average_gemetric(time_list)

    # Для статистики
    file = open('1.txt', 'a')
    file.write('{0}'.format(sa) + ' ' + '{0}'.format(sg) + '\n')

    # процент оценок
    print('Процент оценок:')
    procent_valuation = percentage(valuation_list)

    # Метрика зависимости времени от кол-ва символов


def create_parser_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', type=str, help="generation urls")
    parser.add_argument('-n', type=str, help="use only url_list.py")
    return parser


if __name__ == '__main__':
    parser_arg = create_parser_arg()
    namespace = parser_arg.parse_args(sys.argv[1:])
    y = namespace.y
    n = namespace.n

    if y is not None:
        if n is not None:
            main(False)
        else:
            main(True)
    else:
        test(False)
