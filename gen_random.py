# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
from random import randint

def gen_random(n, min, max):
    for i in range(n):
        yield randint(min, max)



def main():

    rez = gen_random(5, 1, 3)
    for i in rez:
        print(i)
        
if __name__ == "__main__":
    main()