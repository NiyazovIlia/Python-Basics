"""
 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
 и метод running (запуск). Атрибут реализовать как приватный.
 В рамках метода реализовать переключение светофора в режимы:
 красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд,
 второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке
 (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Горит {TrafficLight.__colors[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
