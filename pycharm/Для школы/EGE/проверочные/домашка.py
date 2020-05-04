from random import randint
file = []
tabl = []
score = 0

row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. столбиков: '))
numb = row*col
point = int(input('Введите число для сравнения: '))

def clear_file(file):   #Работает
    for i in range(row):
        file.append(['O']*col)

        
for i in range(numb):
    tabl.append(randint(0, 100))

clear_file(file)

g = 0 
for k in range(row): #Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (numb - 1):
            break
        file[k][j] = tabl[g]
        g+=1

print(file)

g = 0 
for k in range(row): #Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (numb - 1):
            break
        if file[k][j] > point:
            score+=1
        g+=1

print(score)
