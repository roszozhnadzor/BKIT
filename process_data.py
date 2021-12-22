import json
import sys
from field import field
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1
# Сделаем другие необходимые импорты

path = "/Users/mac/Desktop/БКИТ/lab_python_fp/data_light.json"
with open(path, "r", encoding='utf-8') as f:
    data = json.load(f)
# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк
@print_result
def f1(arg):
    return(list(sorted([el for el in Unique(field(arg, 'job-name'), ignore_case=True)])))
@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))
@print_result   
def f3(arg):
    return list(map(lambda x: x + ' со знанием Python', arg))
@print_result
def f4(arg):
    pays = list(zip(arg, list(gen_random(len(arg), 100000, 200000))))
    return list(map(lambda x: x[0] + ", зарплата " + str(x[1]) + " руб.", pays))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))