from random import randint
import time
import matplotlib.pyplot as plt


#ranger = int(input('Длинна массива: '))


def create_mass(minim, maxim, count):
    my_masive = []
    for idx in range(count):  # заполняем массив рандомными элементами
        my_masive.append(randint(minim, maxim))
    return my_masive


def selct_sort(mas):
    for ots in range(len(mas)):
        max_idx = 0
        for idx in range(len(mas) - ots):
            if mas[max_idx] < mas[idx]:
                max_idx = idx
        mas[max_idx], mas[len(mas) - 1 - ots] = mas[len(mas) - 1 - ots], mas[max_idx]
    return mas


def selct_sort_two_side(mas):
    for ots in range(len(mas) // 2):
        max_idx = ots
        min_idx = ots
        for idx in range(ots, len(mas) - ots, 1):
            if mas[max_idx] < mas[idx]:
                max_idx = idx
            if mas[min_idx] > mas[idx]:
                min_idx = idx
        if max_idx == ots and min_idx == len(mas) - 1 - ots:
            mas[max_idx], mas[len(mas) - 1 - ots] = mas[len(mas) - 1 - ots], mas[max_idx]
        elif min_idx == len(mas) - 1 - ots:
            mas[max_idx], mas[len(mas) - 1 - ots] = mas[len(mas) - 1 - ots], mas[max_idx]
            min_idx = max_idx
            mas[min_idx], mas[ots] = mas[ots], mas[min_idx]
        else:
            mas[max_idx], mas[len(mas) - 1 - ots] = mas[len(mas) - 1 - ots], mas[max_idx]
            mas[min_idx], mas[ots] = mas[ots], mas[min_idx]
    return mas



count_elemrnts = [el for el in range(2, 10000, 50)]
time_select = []
time_select_two_side = []

for count in count_elemrnts:
    my_mass = create_mass(1, 1000, count)  ##[37, 26, 2, 10, 27, 36, 22, 5, 12, 14, 2, 3, 29, 10, 3]#
    my_mass_2 = list(my_mass)
    start = time.time()
    selct_sort(my_mass)
    time_select.append(time.time() - start)
    start = time.time()
    selct_sort_two_side(my_mass_2)
    time_select_two_side.append(time.time() - start)
    print('------------')
    print(count)

plt.plot(count_elemrnts, time_select, color='orange')  # Одиночным выбором
plt.plot(count_elemrnts, time_select_two_side, color='purple')  # Двойным выбором
plt.show()
# print(my_mass)
# print(my_mass_2)
