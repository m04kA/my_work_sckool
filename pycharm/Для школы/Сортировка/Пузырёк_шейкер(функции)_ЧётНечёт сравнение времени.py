import time
from random import randint


test = int(input('Количество тестов: '))
ranger = int(input('Длинна массива: '))
my_min = int(input('Min: '))
my_max = int(input('Max: '))

def massive(minim, maxim, count):
    my_masive = []
    for idx in range(count):  # заполняем массив рандомными элементами
        my_masive.append(randint(minim, maxim))
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
    # return spisok


def bubble(file):
    for i in range(len(file) - 1):
        for j in range((len(file) - 1 - i)):
            if file[j] > file[j + 1]:
                file[j], file[j + 1] = file[j + 1], file[j]
    # return file


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
    # return massive


def work(num_min, num_max, count_test, my_len):
    time_buble = 0
    time_sheyker = 0
    time_odd_even = 0
    for _ in range(count_test):
        mas_1 = massive(num_min, num_max, my_len)
        mas_2 = list(mas_1)
        mas_3 = list(mas_1)
        start = time.time()
        bubble(mas_1)
        time_buble += time.time() - start
        start = time.time()
        sheyker(mas_2)
        time_sheyker += time.time() - start
        start = time.time()
        chet_nechet(mas_3)
        time_odd_even += time.time() - start
    time_buble /= count_test
    time_sheyker /= count_test
    time_odd_even /= count_test
    return time_buble, time_sheyker, time_odd_even


tim_bub,tim_shey,tim_odd = work(my_min, my_max, test, ranger)
print(f'Среднее время сортировки пузырьком: {tim_bub}')
print(f'Среднее время сортировки шейкером: {tim_shey}')
print(f'Среднее время сортировки Чётно - нечётной: {tim_odd}')
# msk_1 = massive(0, 500, 3500)
# msk_2 = list(msk_1)
# msk_3 = list(msk_1)
# start = time.time()
# bubble(msk_1)
# print(time.time() - start)
# start = time.time()
# sheyker(msk_2)
# print(time.time() - start)
# start = time.time()
# chet_nechet(msk_3)
# print(time.time() - start)
