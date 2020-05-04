from random import randint
import time
row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. столбцов: '))
tabl = []
times = int(input('Введите время: '))


def clear_tabl(tabl):
    for i in range(row):
      tabl.append([])
      for j in range(col):
            tabl[i].append(randint(1,100))
    
def print_tabl(tabl):
    for n in tabl:
        print(' '. join(str(n)))

def bubble(file):
    for i in range(len(file)-1):
        for j in range((len(file)-1)):
            if file[j] > file[j+1]:
                file[j],file[j+1] = file[j+1],file[j]

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

def maxx(row,col,tabl):
      max_sum = [0, 0]
      for i in range(row):
            sum_row = 0
            for j in range(col):
                  sum_row +=tabl[i][j]
            if max_sum[0]<sum_row:
                  max_sum[0] = sum_row
                  max_sum[1] = i
      print('номер строки с самой большой суммой: '+str(max_sum[1]+1))


start = time.time()
clear_tabl(tabl)
print_tabl(tabl)
for i in range(row):
      if i%2 == 0:
            sheyker(tabl[i])
      elif i%2 != 0:
            bubble(tabl[i])
print('------------')
print_tabl(tabl)
maxx(row,col,tabl)
finish = time.time() - start

if finish > times:
      score = 0
      for i in range(row):
            for j in range(col):
                  if (score+1)%4 ==0:
                        tabl[i][j] = '&'
                        score +=1
                  else:
                        score +=1
print('-----------')
print_tabl(tabl)

                  
      
