from random import randint
import time

my_len_mass = int(input('Введите длинну массива: '))
my_num = int(input('Введите число: '))
test = int(input('Введите количество тестов: '))


def app_mass(len_mass):
    mas = []
    for _ in range(len_mass):
        mas.append(randint(-1000, 1000))
    return mas


def perebor(mass, num):
    znach = False
    for idx in range(len(mass)):
        if mass[idx] == num:
            znach = True
            idx_el = idx
            break
    return znach


def fast(mass, num):
    znach = False
    start = 0
    end = len(mass) - 1
    while start <= end:
        mid = (start + end) // 2
        if mass[mid] == num:
            znach = True
            idx = mid
            break
        elif num < mass[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return znach


my_mass = app_mass(my_len_mass)
my_mass.sort()

start_test_1 = []
end_test_1 = []
start_test_2 = []
end_test_2 = []
for i in range(test):
    start_1 = time.time()
    start_test_1.append(start_1)
    test_01 = perebor(my_mass, my_num)
    end_1 = time.time()
    end_test_1.append(end_1)
    start_2 = time.time()
    start_test_2.append(start_2)
    test_02 = fast(my_mass, my_num)
    end_2 = time.time()
    end_test_2.append(end_2)

strt_1 = 0
for el in start_test_1:
    strt_1 += el
strt_1 = strt_1 / test

en_1 = 0
for el in end_test_1:
    en_1 += el
en_1 = en_1 / test

strt_2 = 0
for el in start_test_2:
    strt_2 += el
strt_2 = strt_2 / test

en_2 = 0
for el in end_test_1:
    en_2 += el
en_2 = en_2 / test

time_work_1 = en_1 - strt_1
time_work_2 = en_2 - strt_2

print(f'Различие перебора от быстрого поиска на: {time_work_1 - time_work_2}')
