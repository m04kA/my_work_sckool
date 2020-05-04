from random import randint
tabl = []
long = int(input('Длинна таблицы: '))
for i in range(long):
    tabl.append(randint(0,1000))

print(tabl)
maxx = [0,0,0]
for i in range(len(tabl)-7):
    for j in range(i+7, len(tabl)):
        if (tabl[i]*tabl[j]) > maxx[0]:
            maxx[0] = tabl[i]*tabl[j]
            maxx[1] = tabl[i]
            maxx[2] = tabl[j]

print('Ответ: '+str(maxx[0])+' Числа: '+str(maxx[1])+ ' '+str(maxx[2]))
        
