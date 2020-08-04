'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''


class Null:
    def __init__(self, delim, delit):
        self.delim = delim
        self.delit = delit

    @staticmethod
    def divide_by_null(delim, delit):
        try:
            return (delim / delit)
        except BaseException:
            return (f"Деление на ноль недопустимо")


div = Null(10, 100)
print(Null.divide_by_null(10, 0))
print(Null.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
