import math

f = open('1.txt')
sa_ = []
sg_ = []
for line in f:
    s = line.split(' ')
    sa_.append(float(s[0]))
    sg_.append(float(s[1]))

summa = 0.0
for c in sa_:
    summa += c
sa = summa / len(sa_)
print("sa: {0}".format(sa))

summa = 0.0
for c in sg_:
    summa += c
sa = summa / len(sg_)
print("sg: {0}".format(sa))


