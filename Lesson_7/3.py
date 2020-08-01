class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        a = self.quantity - other.quantity
        return "*" * a

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)
                       ):  # делим что бы узнать сколько целых частей должно быть
            row += f'{"*" * cells_in_row} \\n '  # добавляем целые части
        # узнаем остатки от деления и добавлемя остатки
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(33)
cells2 = Cell(9)
# print(f"Первая клетка: {cells1}")
# print(f"Вторая клетка: {cells2}")
# print(f"Сложение: {cells1 + cells2}")
# print(f"Вычитание: {cells1 - cells2}")
# print(f"Умножение: {cells1 * cells2}")
print(cells2.make_order(6))
print(cells1.make_order(12))
