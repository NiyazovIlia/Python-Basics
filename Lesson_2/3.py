# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и через dict.

year_month = int(input("Введите число месяца: "))
year_list = ['зима', 'весна', 'лето', 'осень']
year_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if year_month == 12 or year_month == 1 or year_month == 2:
    print(year_list[0])
    print(year_dict.get(1))
elif year_month == 3 or year_month == 4 or year_month == 5:
    print(year_list[1])
    print(year_dict.get(2))
elif year_month == 6 or year_month == 7 or year_month == 8:
    print(year_list[2])
    print(year_dict.get(3))
elif year_month == 9 or year_month == 10 or year_month == 11:
    print(year_list[3])
    print(year_dict.get(4))


# year_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# year_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
# if year_month in year_list[0]:
#     print('Зима')
#     print(year_dict.get(1))
# elif year_month in year_list[1]:
#     print('Весна')
#     print(year_dict.get(2))
# elif year_month in year_list[2]:
#     print('Лето')
#     print(year_dict.get(3))
# elif year_month in year_list[3]:
#     print('Осень')
#     print(year_dict.get(4))