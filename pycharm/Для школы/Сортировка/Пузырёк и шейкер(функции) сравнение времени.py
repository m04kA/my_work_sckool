import time
from random import randint

nums = int(input('Количество тестов: '))

timess1 = 0
timess2 = 0
ranger = int(input('Длинна массива: '))

    

delta = []
ansver = 0.0


def sheyker(spisok):
    left = 0              #Переменная для движения с права на лева
    right = len(spisok)-1 #Переменная для движения с лева на права

    while left <= right:
        for i in range(right):                      #Самый тяжёлый элемент в право
            if spisok[i] > spisok[i+1]:
                spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
        right -=1                                   #Пропускаем самый большой элемент, который уже занял своё место

        for i in range(right,left,-1):              #Самый лёгкий элемент в лево
            if spisok[i] < spisok[i-1]:
                spisok[i],spisok[i-1] = spisok[i-1],spisok[i]    
        left +=1                                    #Пропускаем самый лёгкий элемент, занявший своё место


def bubble(file):
    for i in range(len(file)-1):
        for j in range((len(file)-1-i)):
            if file[j] > file[j+1]:
                file[j],file[j+1] = file[j+1],file[j]
    

for k in range(nums):
    
    file = []
    for i in range(ranger):       #Заполнение массива
        file.append(randint(1,10000))
    file1 = file

    start = time.time()
    bubble(file)
    timess1 = time.time() - start
    print('time_bubble=' + str(timess1))


    start = time.time()
    sheyker(file1)
    timess2 = time.time() - start
    print('time_sheyker=' + str(timess2))

    delta.append(abs(timess1-timess2))

for i in range(len(delta)):
    ansver = ansver+delta[i]

ansver = ansver/len(delta)
print('Среднее арифметическое всех дельт: ' + str(ansver))
