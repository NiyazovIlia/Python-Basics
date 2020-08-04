# ----------------------------------- 4 ----------------------------------
'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

# ----------------------------------- 5 ----------------------------------

'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.
'''

# ----------------------------------- 6 ----------------------------------
'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''


class OrgTechnics:
    def __init__(self, name, height, weight, count):
        self.name = name
        self.height = height
        self.weight = weight
        self.count = count


class Printer(OrgTechnics):
    def __init__(self, name, height, weight, count, color):
        super().__init__(name, height, weight, count)
        self.color = color

    def add(self):
        add_printer = []

        if self.color == 'белый':
            return f'Увы принтер с цветом {self.color} не бывает'
        else:
            add_printer.append(
                [self.name, self.height, self.weight, self.count, self.color])
            return add_printer


class Scaner(OrgTechnics):
    def __init__(self, name, height, weight, count, pixel):
        super().__init__(name, height, weight, count)
        self.pixel = pixel

    def add(self):
        add_scaner = []
        if self.name == 'HP':
            return f'Увы но компания {self.name} мы не производим'
        else:
            add_scaner.append(
                [self.name, self.height, self.weight, self.count, self.pixel])
            return add_scaner


class Kseros(OrgTechnics):
    def __init__(self, name, height, weight, count, speed):
        super().__init__(name, height, weight, count)
        self.speed = speed

    def add(self):
        add_kseros = []

        if self.height == '250':
            return f'Увы но ксерос {self.name} с высотой {self.height} слишком большой'
        else:
            add_kseros.append(
                [self.name, self.height, self.weight, self.count, self.speed])
            return add_kseros


class Fold:
    while True:
        type = input("Какой тип товара (принтер, сканер или ксерос): ")
        if type.lower() == "принтер":
            a = Printer(
                input("Имя:"),
                input("Высота: "),
                input("Ширина: "),
                input("Колличество: "),
                input("Цвет: "),)
            print(a.add())
        elif type.lower() == "сканер":
            a = Scaner(
                input("Имя:"),
                input("Высота: "),
                input("Ширина: "),
                input("Колличество: "),
                input("Пикеселей: "))
            print(a.add())
        elif type.lower() == "ксерос":
            a = Kseros(
                input("Имя:"),
                input("Высота: "),
                input("Ширина: "),
                input("Колличество: "),
                input("Скорость: "))
            print(a.add())


Fold()
