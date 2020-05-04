from random import randint
n = int(input('Введите кол. чисел: '))
a = []

for i in range(n):
    a.append(int(input())) #randint(2,12000)
    
print(a)
maxx = [0,0,0]
for i in range(n-1):
    for j in range(n):
        if i < j and a[i]>a[j] and (a[i]+a[j])%120==0 and (a[i]+a[j])>maxx[0]:
            maxx[0] = a[i]+a[j]
            maxx[1] = a[i]
            maxx[2] = a[j]

print(str(maxx[1])+ ' '+str(maxx[2]))


    
                    
        
