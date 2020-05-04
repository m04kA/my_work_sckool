kod_slovo = 'командир'
fraz = 'автором метода является Уитстон'
fraz = fraz.split()
alfovit = 'абвгдежзиклмнопрстуфхцчшщьыэюя'
tabl = []
row = 5
col = 6
answ = ''

def print_tabl(tabl):
    for n in tabl:
        print(' '. join(n))
        
def create_tabl(tabl, row, col):
    for i in range(row):
        tabl.append(['O']*col)  #Создание и заполнение пустышками таблицу

def bigramm(fraz):
    bigrama = ''
    for i in range(len(fraz)):
        for k in range(len(fraz[i])-1):
            if fraz[i][k] == fraz[i][k+1]:   #Если 2 одинаковых символа рядом
                fraz[i][:k+1] + 'ф' + fraz[i][k+1:]
        if len(fraz[i])%2 != 0:                #Если нечётное кол. символов
            fraz[i] +='ф'                          #Ф - пустышка

    for i in range(len(fraz)):
        for j in range(0,len(fraz[i]), 2):
            bigrama +=  fraz[i][j] + fraz[i][j+1]+' '
    return bigrama


#create_tabl(tabl, row, col)
print_tabl(tabl)

n = 0
m = 0
print(fraz)
for k in range(row): #Переходим на следующую строчку
    tabl.append([])
    for j in range(col):  # Заполняем строчку
        if n< len(kod_slovo) :
               
            tabl[k].append(kod_slovo[n])
            if kod_slovo.find(kod_slovo[n]) != n :
                n += 1
                continue
            else:
                alfovit = alfovit[:alfovit.find(kod_slovo[n])] + alfovit[alfovit.find(kod_slovo[n])+1:]
                n +=1
        else:
            tabl[k].append(alfovit[m])
            m +=1

print_tabl(tabl)

for i in range(len(fraz)):
    for k in range(len(fraz[i])-1):
        if fraz[i][k] == fraz[i][k+1]:
            fraz[i][:k+1] + 'ф' + fraz[i][k+1:]
    if len(fraz[i])%2 != 0:
        fraz[i] +='ф' #Ф - пустышка

index_1 = [0, 0]
index_2 = [0, 0]
bigrama = ''

for i in range(len(fraz)):
    for j in range(0,len(fraz[i]), 2):
        bigrama +=  fraz[i][j] + fraz[i][j+1]+' '
        for k in range(row):
            for n in range(col):
                if fraz[i][j] == tabl[k][n]:
                    index_1[0] = k
                    index_1[1] = n
                if fraz[i][j+1] ==tabl[k][n]:
                    index_2[0] = k
                    index_2[1] = n
        if index_1[0] == index_2[0] and index_1[1] != index_2[1]:
            if index_1[1] == col-1:
                answ += tabl[index_1[0]][0] + tabl[index_2[0]][index_2[1]+1] + ' '
                continue
            elif index_2[1] == col-1:
                answ += tabl[index_1[0]][index_1[1]+1] + tabl[index_2[0]][0] + ' '
                continue
            answ += tabl[index_1[0]][index_1[1]+1] + tabl[index_2[0]][index_2[1]+1] + ' '#answ += tabl[index_1[0]][index_1[1]] + tabl[index_2[0]][index_2[1]] + ' '
        elif index_1[0] != index_2[0] and index_1[1] == index_2[1]:
            if index_1[0] == row-1:
                answ += tabl[0][index_1[1]] + tabl[index_2[0]+1][index_2[1]] + ' '
                continue
            elif index_2[0] == row-1:
                answ += tabl[index_1[0]+1][index_1[1]] + tabl[0][index_2[1]] + ' '
                continue
            answ += tabl[index_1[0]+1][index_1[1]] + tabl[index_2[0]+1][index_2[1]] + ' '
        elif index_1[0] != index_2[0] and index_1[1] != index_2[1]:
            answ += tabl[index_1[0]][index_2[1]] + tabl[index_2[0]][index_1[1]] + ' '

print('     ')
print(bigrama)
print(answ)

#Исправить ошибку с перемещением букв вниз с возвращением на верх(проблема с индексами по переносу)


            
            
    
