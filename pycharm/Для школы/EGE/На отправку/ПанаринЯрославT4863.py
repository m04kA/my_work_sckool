from random import randint
a = [60, 47, 27, 95,54]
N = 2018

#for i in range(N):
 #   a.append(int(randint(1, 150)))

k = min(a)

for i in range(len(a)):
    if a[i] < k*2:
        a[i] = a[i]*2
print(a)
