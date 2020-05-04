from random import randint
tabl = []
row = int(input('Введите количество строк: '))
col = int(input('Введите количество символов в строке: '))

def cleate_tabl(tabl):
    for i in range(row):
      tabl.append([])
      for j in range(col):
            tabl[i].append(randint(-1000,1000))

def bubble(tabl):
    for i in range(len(tabl)-1):
        for j in range((len(tabl)-1)):
            if tabl[j] > tabl[j+1]:
                tabl[j],tabl[j+1] = tabl[j+1],tabl[j]

def sheyker(tabl):
        left = 0              
        right = len(tabl)-1 

        while left <= right:
            for i in range(right):                      
                if tabl[i] > tabl[i+1]:
                    tabl[i],tabl[i+1] = tabl[i+1],tabl[i]
            right -=1

            for i in range(right,left,-1):              
                if tabl[i] < tabl[i-1]:
                    tabl[i],tabl[i-1] = tabl[i-1],tabl[i]    
            left +=1

def minn(tabl,row):
    mi = 1000000
    for i in range(row):
        if min(tabl[i]) < mi:
            mi = min(tabl[i])
    return mi

def print_tabl(tabl):
    for n in tabl:
        print(' '. join(str(n)))

def arifmet(tabl, row, col):
    arifm = 0
    score = row*col
    for i in range(row):
        for j in range(col):
            arifm += tabl[i][j]
    return arifm/score

            
            

cleate_tabl(tabl)
print_tabl(tabl)
for i in range(row):
      if i%2 == 0:
          bubble(tabl[i])
      elif i%2 != 0:
            sheyker(tabl[i])
print('       ')
print_tabl(tabl)
minim = minn(tabl, row)
sredn = arifmet(tabl, row, col)
print(minim)
print(sredn)

def bol_sr(tabl, row, col, sredn):
    for i in range(row):
        for j in range(col):
            if tabl[i][j] > sredn:
                tabl[i][j] = '&'
bol_sr(tabl, row, col, sredn)
print_tabl(tabl)
                












