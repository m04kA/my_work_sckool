from random import randint
import random
fraza = input('Введите вашу фразу: ')
tabl = [] #Таблица, где будут разделение по ячейкам
col = int(input('Введите кол. столбиков: ')) #Столбики (кол. символов в 1-й строке)
row = int(input('Введите кол. строк: ')) #Строки
cols = []
def print_tabl(tabl):
    for n in tabl:
        print(' '. join(n))

for i in range(row):
    tabl.append(['O']*col)  #Создание и заполнение пустышками таблицу

print_tabl(tabl)
print('  ')
g = 0 #Переменная для заполнения символами табл
for k in range(row): #Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (len(fraza) - 1):
            break
        if fraza[g] == ' ': #Проверка и пропуск пробела
            g += 1
        #print(k, j, g, (len(fraza)) - 1) #Для отладки работы программы
        tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
        g += 1
print_tabl(tabl)
print('   ')

g = 0
for k in range(row): #Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (len(fraza) - 1):
            tabl[k][j] = '' #Удаляем лишние ячейки для вывода шифра
        g += 1
a =[]
for i in range(col): # Заолнение массива кол.
    cols.append(i)
    a.append(i)

random.shuffle(a)

    
print('  ')
ansv = ''
counter = 0
for k in range(col):
        
    for j in range(row):
        ansv = ansv + str(tabl[j][cols[a[counter]]])
    
    counter +=1

print(ansv)



