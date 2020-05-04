from random import randint
file = []
tabl = []

row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. столбиков: '))
numb = row*col


        
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

for n in range(row):
    if n%2==0:
        for i in range(col):
            for j in range(col-1):
                if file[n][j] > file[n][j+1]:
                    file[n][j],file[n][j+1] = file[n][j+1],file[n][j]
    elif n%2!=0:
        for i in range(col-1, -1, -1):
            for j in range(col-2, -1, -1):
                if file[n][j] < file[n][j+1]:
                    file[n][j],file[n][j+1] = file[n][j+1],file[n][j]

print(file)        
        

