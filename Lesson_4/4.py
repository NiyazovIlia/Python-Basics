# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import random

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_new_list = [el for el in my_list if my_list.count(el) == 1]
# print(my_new_list)


a = int(input("Скольок чисел будет в массиве: "))
array = []
while a > 0:
    array.append(random.randint(0, 100))
    a -= 1
print(array)

new_array = [i for i in array if array.count(i) == 1]
print(new_array)