# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.


def people(name, surname, data, city, email, telephone):
    return f"\nИмя: {name}\n" \
           f"Фамилия: {surname}\n" \
           f"Год рождения: {data}\n" \
           f"Город проживания: {city}\n" \
           f"email: {email}\n" \
           f"Телефон: {telephone}"


if __name__ == '__main__':
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    data = input("Введите год рождения: ")
    city = input("Введите ваш город в котором вы проживаете: ")
    email = input("Введите вашу почту: ")
    telephone = input("Введите ваш номер телефона: ")

    print(people(name, surname, data, city, email, telephone))