import math

from tests.graphics import lineplot

time_list = [3.917, 0.934, 0.339, 1.013, 0.306, 1.433, 0.234, 0.22, 0.775, 0.308]


lineplot(x_data=[i for i in range(1, len(time_list) + 1)], y_data=time_list, x_label='site(count)', y_label='time', name='time')


summa=0.0
for c in time_list:
    summa+=c
sa = summa / len(time_list)
print("Средне арифмитическое:{0}".format(sa))


mno = 1.0
for c in time_list:
    mno *= c
print("Средне геометрическое:{0}".format(math.pow(mno, 1 / len(time_list))))