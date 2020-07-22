# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, 
# при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def my_count_func(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iterrator = cycle(my_list)
    while i < iteration:
        print(next(iterrator))
        i += 1


my_count_func(int(input("Начальное число: ")), int(input("Конечное число: ")))
my_cycle_func(my_list=[1, 2], iteration=int(input("Сколько вывести раз: ")))
