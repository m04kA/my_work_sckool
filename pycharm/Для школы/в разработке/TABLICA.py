tab = [['','А','Б','В','Г','Д','Ж','З'],
       ['А','0','1','1','0','0','1','0'],
       ['Б','0','0','0','1','0','1','1'],
       ['В','0','0','0','0','1','1','1'],
       ['Г','0','0','0','0','0','0','1'],
       ['Д','0','0','0','0','0','0','1'],
       ['Ж','0','0','0','0','0','0','1'],
       ['З','0','0','0','0','0','0','0']]

start = input('ведите точку начала: ').upper()
end = input('ведите точку конца: ').upper()
kol_vo = []
st = 0 #Значение строки стартовой точки
progon = 0

def find_strok(tab, start):    
    for j in range(len(tab[0])):
        for i in range(len(tab[0])):
            if tab[0][i] == start:
                col = i
    return col

def find_one(tab, kol_vo, st):
    for j in range(len(tab[st])):
        if tab[st][j] == '1':
            kol_vo.append(tab[0][j])
    return kol_vo

st = find_strok(tab, start)
find_one(tab, kol_vo, st)
print(st)
print(kol_vo)

#while 
#progon = len(kol_vo)
#for i in range(progon):
#    start = kol_vo[i]
#    st = find_strok(tab, start)

            

                   
