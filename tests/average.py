import math
from collections import Counter


def average_arithmetic(list_, prnt=True):
    summa = 0.0
    for c in list_:
        summa += c
    sa = round(summa / len(list_), 2)
    if prnt:
        print("Средне арифмитическое:{0}".format(sa))
    return sa


def average_gemetric(list_, prnt=True):
    mno = 1.0
    for c in list_:
        mno *= c
    sg = round(math.pow(mno, 1 / len(list_)), 2)
    if prnt:
        print("Средне геометрическое:{0}".format(sg))
    return sg


def percentage(list_, prnt=True):
    c = Counter(list_)
    for k in c.keys():
        tmp = c[k]
        c[k] = round(tmp / len(list_) * 100, 1)
        if prnt:
            print('{0}: {1}'.format(k, c[k]))
    return c


x_data = [i for i in range(1, 20)]