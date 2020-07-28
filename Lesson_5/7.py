profit = {}
avarage_summ = {}
prof = 0
new_prof = 0
i = 0
with open('file_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        new_prof = prof / i
        print(f'Прибыль средняя - {new_prof:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    avarage_summ = {'средняя прибыль': round(new_prof)}
    profit.update(avarage_summ)
    print(f'Прибыль каждой компании - {profit}')