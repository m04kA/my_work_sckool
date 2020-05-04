from random import randint
que = input('Для шифрования введите (1), для  дешифрования введите (0): ')
fraza = input('Введите вашу фразу: ')
tabl = [] #Таблица, где будут разделение по ячейкам
col = int(input('Введите кол. столбиков: ')) #Столбики (кол. символов в 1-й строке)
row = int(input('Введите кол. строк: ')) #Строки
ansv = '' #Ответ кодировки
tabl_decod = [] #Декодированная таблица
de_fraz = '' # Декодированная фраза
alfovit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #Русский алфовит

def print_tabl(tabl):
    for n in tabl:
        print(' '. join(n))

def create_tabl(tabl):
    for i in range(row):
        tabl.append(['O']*col)  #Создание и заполнение пустышками таблицу

def test(k, j, g, fraza):
    print('Строчка '+str(k), 'СТолбик '+str(j), 'Символ фразы '+str(g), 'Длинна фразы '+str((len(fraza)) - 1)) #Для отладки работы программы

def surplus(row, col, fraza, tabl):   #Чистка
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

def coder(row,col,tabl, ansv):
    coup = True #Для переворота строки
    for j in range(col):
        if coup == True:   #Снизу вверх
            for k in range(row):
                ansv = ansv + str(tabl[k][j])
            coup = False
        else:  #Сверху вниз
            for k in range(row-1, -1, -1):
                ansv = ansv + str(tabl[k][j])
            coup = True
    return ansv

def content(row,col,fraza,tabl):
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

def dekoder_tabl(row, col, ansv, tabl_decod):
    g = 0 #Для заполнения таблицы
    create_tabl(tabl_decod)
    coup = True #Для переворота стoлбца
    for j in range(col):
        if coup == True:   #Снизу вверх
            for k in range(row):
                if g > (len(ansv)-1):
                    break
                tabl_decod[k][j] = ansv[g]
                g +=1
            coup = False
        else:  #Сверху вниз
            for k in range(row-1, -1, -1):
                if g > (len(ansv)-1):
                    break                
                tabl_decod[k][j] = ansv[g]
                g +=1
            coup = True

def decod_fraz(row, col, tabl_decod, de_fraz):
    for i in range(row):
        if i%2 == 0:
            for j in range(col):
                de_fraz += tabl_decod[i][j]
        elif i%2 != 0:
            for j in range(col-1,-1,-1):
                de_fraz += tabl_decod[i][j]
    return de_fraz

def tablica_2(tabl, alfovit, col, row):
    for k in range(row):  #Создание таблицы(*)
        tabl.append([])
        for j in range(col):  
            tabl[k].append('*')
            
    for i in range(33):  #Рандомное заполнение буквами
        a = False
        while a == False:
            y = randint(0, row-1)
            x = randint(0, col-1)
            rand = randint(0, len(alfovit)-1)
            if tabl[y][x] == '*':
                tabl[y][x] = alfovit[rand]
                alfovit = alfovit[:rand] + alfovit[rand+1:]
                a = True

    for i in range(row):     #Заполнение оставшихся ячеек 5
        for j in range(col):
            if tabl[i][j] == '*':
                tabl[i][j] = '5'
                     
    return tabl

def ans(answer, ansv, tabl, row, col):
    dlin = len(ansv)
    for k in range(dlin):
        for i in range(row):
            for j in range(col):
                if ansv[k] == tabl[i][j]:
                    answer = answer + str(i) + str(j)
    return answer




    
if que == '1':
    create_tabl(tabl)
    print_tabl(tabl)
    print('  ')

    content(row,col,fraza,tabl)
    print_tabl(tabl)

    surplus(row, col, fraza, tabl)
    print('   ')
    
    ansv = coder(row,col,tabl, ansv)
    print(ansv)
    print('   ')

    tablica = [] #2-я таблица
    strok = int(input('Введите кол. строк в новой табл.: '))
    colonk = int(input('Введите кол. столбцов в новой табл.: '))
    answer = '' #Закодированный ответ(цифры)

    tablica = tablica_2(tablica, alfovit, colonk, strok)
    print_tabl(tablica)

    answer = ans(answer, ansv, tablica, strok, colonk)
    print(answer)    

elif que == '0':
    dekoder(row, col, ansv, tabl_decod)
    print_tabl(tabl_decod)
    de_fraz = decod_fraz(row, col, tabl_decod, de_fraz)
    print(de_fraz)
