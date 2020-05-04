from random import randint
tabl = []
numbers = []
minim = 101
maxim = 1
col = int(input('Введите кол. столбиков: ')) #Столбики (кол. символов в 1-й строке)
row = int(input('Введите кол. строк: ')) #Строки
def print_tabl(tabl):
    for n in tabl:
        print(' '. join(n))

for i in range(row):
    tabl.append(['O']*col)  #Создание и заполнение пустышками таблицу


print_tabl(tabl)
print('  ')


for k in range(row): #Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        tabl[k][j] = str(randint(1, 100))  # Основа, заполняюзая таблицу

print_tabl(tabl)

for k in range(row): #Ищем минимум
    for j in range(col):
        tabl[k][j] = int(tabl[k][j])
        if minim > tabl[k][j]:
            minim = tabl[k][j]

for k in range(row): #Ищем минимум
    for j in range(col):
        tabl[k][j] = int(tabl[k][j])
        if maxim < tabl[k][j]:
            maxim = tabl[k][j]

print('Максимум', maxim)
print('Минимум', minim)
print('  ')

for k in range(row): #Ищем минимум
    for j in range(col):
        if k == j:
            tabl[k][j] = 'X'
        else:
            tabl[k][j] = 'O'
print_tabl(tabl)
