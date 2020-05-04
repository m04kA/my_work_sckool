import sys
from itertools import count
from itertools import cycle


def sequence(numb):
    numbs = []
    for el in count(numb):
        if len(numbs) <= 5:
            numbs.append(el)
        else:
            break

    с = 0
    for el in cycle(numbs):
        if с > 1:
            break
        с += 1
        answer = el

    return answer


if len(sys.argv) == 2:
    my_num = sys.argv[1:]
else:
    my_num = int(input('Введите число: '))
print(f"Вот число из списка: {sequence(my_num)}")
