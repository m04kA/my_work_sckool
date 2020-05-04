
fraza = input('Введите вашу фразу: ').split()
fraza = ''.join(fraza)
tabl = [] #Таблица, где будут разделение по ячейкам
col = int(input('Введите кол. столбиков: ')) #Столбики (кол. символов в 1-й строке)
row = int(input('Введите кол. строк: ')) #Строки

def print_tabl(tabl):
    for n in tabl:
        print(' '. join(n))

def clear_tabl(tabl):
    for i in range(row):
        tabl.append(['O']*col)  #Создание и заполнение пустышками таблицу

def test(k, j, g, fraza):
    print('Строчка '+str(k), 'СТолбик '+str(j), 'Символ фразы '+str(g), 'Длинна фразы '+str((len(fraza)) - 1)) #Для отладки работы программы

def surplus(row, col, fraza, tabl):
    g = 0
    for k in range(row): #Переходим на следующую строчку
        if k%2 ==0:
            for j in range(col):  # Заполняем строчку
                if g > (len(fraza) - 1):
                    tabl[k][j] = '' #Удаляем лишние ячейки для вывода шифра
                g += 1
        elif k%2 != 0:
            for j in range(col-1, -1, -1):
                if g > (len(fraza) - 1):
                    tabl[k][j] = '' #Удаляем лишние ячейки для вывода шифра
                g += 1

    

clear_tabl(tabl)

print_tabl(tabl)
print('  ')


g = 0 #Переменная для заполнения символами табл

for k in range(row):        #Переходим на следующую строчку  
    if k%2 ==0:
        for j in range(col):     # Заполняем строчку
            if g > (len(fraza) - 1):   #Проверка на конец фразы
                break         
            if fraza[g] == ' ': #Проверка и пропуск пробела
                g += 1
            #test(k, j, g, fraza)
            
            tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
            g += 1
        
        
    elif k%2 != 0:
        for j in range(col-1, -1, -1):     # Заполняем строчку в обратном порядке
            if g > (len(fraza) - 1):   #Проверка на конец фразы
                break
            if fraza[g] == ' ': #Проверка и пропуск пробела
                g += 1
            #test(k, j, g, fraza)
            tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
            g += 1
    

print_tabl(tabl)
#Чистка таблицы
surplus(row, col, fraza, tabl)


print('   ')
ansv = ''
a = True
for j in range(col-1, -1,-1):
    if a == True:
        for k in range(row):
            ansv = ansv + str(tabl[k][j])
        a = False
    else:
        for k in range(row-1, -1, -1):
            ansv = ansv + str(tabl[k][j])
        a = True
print(ansv)
