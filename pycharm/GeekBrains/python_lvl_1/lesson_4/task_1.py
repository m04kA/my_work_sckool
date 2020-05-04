import sys


def zp(*args):
    return args[0]*args[1]+args[2]


if len(sys.argv) == 4:
    print(sys.argv)
    el = sys.argv[1:]
else:
    el = []
    # for idx in range(3): # Можно так, но это без уточнения значений.
    el.append(input('Введите выработку в часах: '))
    el.append(input('Введите ставка в час: '))
    el.append(input('Введите премия: '))

print(f'Вот ваша зарплата: {zp(*map(int, el))}')
