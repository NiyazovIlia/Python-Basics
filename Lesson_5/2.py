# 2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой
# строке.

with open("test_2.txt", "r") as f:
    line = 1
    letters = 0
    for i in f:
        line += i.count("\n")
        letters = len(i.split())
        print(f"{letters} слов в троке")
    print(f"Всего строк {line}")