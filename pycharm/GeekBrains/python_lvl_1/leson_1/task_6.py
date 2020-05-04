# start = float(input('Введите начальный результат спортсмена: '))
start = 2
# finish = float(input('Введите желаемый результат: '))
finish = 3
day = 1
while start < finish:
    print(f'День-{day};Результат-{round(start, 2)}')
    day += 1
    start = start * 1.1
print('--------------------------')
print(f'Результат достигнут к {day} дню, результат: {round(start, 2)}')
