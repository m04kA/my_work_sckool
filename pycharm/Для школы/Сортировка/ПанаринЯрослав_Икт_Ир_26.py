import time
from random import randint
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3825)


def create_random(minim, maxim, count):
    my_masive = []
    for idx in range(count):  # заполняем массив рандомными элементами
        my_masive.append(randint(minim, maxim))
    return my_masive


def create_invert(count):
    my_masive = []
    for idx in range(count, 0, -1):  # заполняем массив рандомными элементами
        my_masive.append(idx)
    return my_masive


def sheyker(spisok):
    left = 0  # Переменная для движения с права на лева
    right = len(spisok) - 1  # Переменная для движения с лева на права
    polog = True

    while polog:
        polog = False
        for i in range(left, right, +1):  # Самый тяжёлый элемент в право
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                polog = True
        if not polog:  # остановка на случай отсортированного массива
            break
        polog = False
        right -= 1  # Пропускаем самый большой элемент, который уже занял своё место

        for i in range(right, left, -1):  # Самый лёгкий элемент в лево
            if spisok[i] < spisok[i - 1]:
                spisok[i], spisok[i - 1] = spisok[i - 1], spisok[i]
                polog = True
        left += 1  # Пропускаем самый лёгкий элемент, занявший своё место
    return spisok


def chet_nechet(massive):
    pologenie = False
    while not pologenie:
        pologenie = True
        for num in range(1, len(massive) - 1, 2):
            if massive[num] > massive[num + 1]:
                massive[num], massive[num + 1] = massive[num + 1], massive[num]
                pologenie = False
        for num in range(0, len(massive) - 1, 2):
            if massive[num] > massive[num + 1]:
                massive[num], massive[num + 1] = massive[num + 1], massive[num]
                pologenie = False
    return massive


def bubble(file):
    for i in range(len(file) - 1):
        for j in range((len(file) - 1 - i)):
            if file[j] > file[j + 1]:
                file[j], file[j + 1] = file[j + 1], file[j]
    return file


def quickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[len(A) - 1]  # random.choice(A)
        Left = []
        Middle = []
        Right = []
        for elem in A:
            if elem < q:
                Left.append(elem)
            elif elem > q:
                Right.append(elem)
            else:
                Middle.append(elem)
        return quickSort(Left) + Middle + quickSort(Right)


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


def merger(mass):
    if len(mass) < 2:
        return mass[:]
    else:
        left_mass = merger(mass[:len(mass) // 2])
        right_mass = merger(mass[len(mass) // 2:])
        return merger_help(left_mass, right_mass)


def merger_help(left_side, right_side):
    answ = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_side) and right_idx < len(right_side):
        if left_side[left_idx] < right_side[right_idx]:
            answ.append(left_side[left_idx])
            left_idx += 1
        elif left_side[left_idx] > right_side[right_idx]:
            answ.append(right_side[right_idx])
            right_idx += 1
        else:
            answ.append(right_side[right_idx])
            answ.append(left_side[left_idx])
            right_idx += 1
            left_idx += 1
    while left_idx < len(left_side):
        answ.append(left_side[left_idx])
        left_idx += 1
    while right_idx < len(right_side):
        answ.append(right_side[right_idx])
        right_idx += 1
    return answ


def insertion(mass):
    for idx_el_compare in range(len(mass)):
        el_in_mass = idx_el_compare - 1
        key_el = mass[idx_el_compare]
        while mass[el_in_mass] > key_el and el_in_mass >= 0:
            mass[el_in_mass + 1] = mass[el_in_mass]
            el_in_mass -= 1
        mass[el_in_mass + 1] = key_el
    return mass


def insertion_together(mass):
    if len(mass) % 2 == 0:
        for k in range(0, len(mass), 2):
            el_1 = k
            el_2 = k + 1
            bufer_1 = mass[k]
            bufer_2 = mass[k + 1]
            if bufer_1 > bufer_2:
                bufer_2 = mass[k]
                bufer_1 = mass[k + 1]
            for i in range(k - 1, -1, -1):
                if mass[i] > bufer_2:
                    mass[el_2] = mass[i]
                    # print(mass)
                    el_2 -= 1
                    el_1 -= 1
                elif mass[i] > bufer_1:
                    mass[el_1] = mass[i]
                    # print(mass)
                    el_1 -= 1
                else:
                    break
                # print('--------')
            mass[el_1] = bufer_1
            mass[el_2] = bufer_2
        return mass
    else:
        for k in range(0, len(mass) - 1, 2):
            el_1 = k
            el_2 = k + 1
            bufer_1 = mass[k]
            bufer_2 = mass[k + 1]
            if bufer_1 > bufer_2:
                bufer_2 = mass[k]
                bufer_1 = mass[k + 1]
            for i in range(k - 1, -1, -1):
                if mass[i] > bufer_2:
                    mass[el_2] = mass[i]
                    # print(mass)
                    el_2 -= 1
                    el_1 -= 1
                elif mass[i] > bufer_1:
                    mass[el_1] = mass[i]
                    # print(mass)
                    el_1 -= 1
                else:
                    break
                # print('--------')
            mass[el_1] = bufer_1
            mass[el_2] = bufer_2

        el_2 = len(mass) - 1
        for i in range(len(mass) - 2, -1, -1):
            if mass[i] > mass[el_2]:
                mass[i], mass[el_2] = mass[el_2], mass[i]
                el_2 -= 1
            else:
                break
        return mass


count_elemrnts = [el for el in range(2, 3803, 100)]
time_bubble = []
time_sheyker = []
time_chet_nechet = []
time_select = []
time_select_two_side = []
time_insertion = []
time_insertion_together = []
time_merger = []
time_quickSort = []

for el in count_elemrnts:
    first_mas = create_invert(el)
    second_mas = list(first_mas)
    third_mas = list(first_mas)
    fourth_mas = list(first_mas)
    fifth_mas = list(first_mas)
    sixth_mas = list(first_mas)
    seventh_mas = list(first_mas)
    eighth_mas = list(first_mas)
    ninth_mas = list(first_mas)

    start = time.time()
    first_mas = bubble(first_mas)
    time_bubble.append(time.time() - start)
    start = time.time()
    second_mas = sheyker(second_mas)
    time_sheyker.append(time.time() - start)
    start = time.time()
    third_mas = chet_nechet(third_mas)
    time_chet_nechet.append(time.time() - start)
    start = time.time()
    fourth_mas = selct_sort(fourth_mas)
    time_select.append(time.time() - start)
    start = time.time()
    fifth_mas = selct_sort_two_side(fifth_mas)
    time_select_two_side.append(time.time() - start)
    start = time.time()
    sixth_mas = insertion(sixth_mas)
    time_insertion.append(time.time() - start)
    start = time.time()
    seventh_mas = insertion_together(seventh_mas)
    time_insertion_together.append(time.time() - start)
    start = time.time()
    eighth_mas = merger(eighth_mas)
    time_merger.append(time.time() - start)

    start = time.time()
    ninth_mas = quickSort(ninth_mas)
    time_quickSort.append(time.time() - start)
    print('------------')
    print(el)

plt.plot(count_elemrnts, time_bubble, color='black', label='Пузырёк')
plt.plot(count_elemrnts, time_sheyker, color='red', label='Шейкер')
plt.plot(count_elemrnts, time_chet_nechet, color='blue', label='Чёт-нечёт')
plt.plot(count_elemrnts, time_select, color='orange', label='Выбором')
plt.plot(count_elemrnts, time_select_two_side, color='green', label='Двойным выбором')
plt.plot(count_elemrnts, time_quickSort, color='yellow', label='Быстрая')
plt.plot(count_elemrnts, time_merger, color='pink', label='Слиянием')
plt.plot(count_elemrnts, time_insertion, color='grey', label='Вставкой')
plt.plot(count_elemrnts, time_insertion_together, color='cyan', label='Двойными вставками')
plt.legend(loc='upper left')
plt.show()
