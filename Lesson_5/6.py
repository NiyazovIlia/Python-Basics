subj = []
with open('file_6.txt', encoding='utf-8') as init_f:
    for line in init_f:
        result = ''.join((i if i in '0123456789' else ' ')
                         for i in line)  # добавляем если входят цифры иначе пробел
        new_result = [int(i) for i in result.split()]
        print(f'{line.split()[0]} {sum(new_result)}')
