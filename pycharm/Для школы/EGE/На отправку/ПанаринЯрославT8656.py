from random import randint
a = [4, -115, 7, 195, 25, -106]
n = 6
#for i in range(n):
 #   a.append(randint(-10000, 10000))

k = a[0]
for i in range(len(a)):
    if a[i]%2 == 0 and a[i] > k:
        k = a[i]
for i in range(len(a)):
    if a[i]%2 == 0:
        a[i] = k
    print(a[i])
