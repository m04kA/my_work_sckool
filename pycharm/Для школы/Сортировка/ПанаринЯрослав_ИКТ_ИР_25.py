import time
from random import randint
import matplotlib.pyplot as plt

#ranger = int(input('Длинна массива: '))


def create(minim, maxim, count):
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
    return spisok


def bubble(file):
    for i in range(len(file) - 1):
        for j in range((len(file) - 1 - i)):
            if file[j] > file[j + 1]:
                file[j], file[j + 1] = file[j + 1], file[j]
    return file


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


count_elemrnts = [el for el in range(2, 15000, 70)]
time_bubble = []
time_sheyker = []
time_chet_nechet = []

for el in count_elemrnts:
    first_mas = create(1, 1000, el)
    second_mas = list(first_mas)
    third_mas = list(first_mas)
    start = time.time()
    bubble(first_mas)
    time_bubble.append(time.time() - start)
    start = time.time()
    sheyker(second_mas)
    time_sheyker.append(time.time() - start)
    start = time.time()
    chet_nechet(third_mas)
    time_chet_nechet.append(time.time() - start)
    print('------------')
    print(el)

plt.plot(count_elemrnts, time_bubble, color='black', label='Пузырёк')  # Пузырьком
plt.plot(count_elemrnts, time_sheyker, color='red', label='Шейкер')  # Шейкером
plt.plot(count_elemrnts, time_chet_nechet, color='blue', label='Чёт-нечёт')  # Чётно-нечётным
plt.legend(loc='upper left')
plt.show()
