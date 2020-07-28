# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

my_list = []
while True:
    one = input("Введите что-нибдуь: ")
    if one == "":
        print(my_list)
        exit()
    else:
        new_list = one + '\n'
        my_list.append(new_list)

    with open("test_1.txt", "w") as f:
        f.writelines(my_list)