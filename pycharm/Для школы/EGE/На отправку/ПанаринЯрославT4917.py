from random import randint
a = [30, 99, 47, 90, 60]
N = 2018
k = a[0]
#for i in range(N):
 #   a.append(int(randint(1, 150)))
for i in range(len(a)):
    if a[i]%5 == 0 and a[i] < k:
        k = a[i]

for i in range(len(a)):
    if a[i]%2 == 1:
        a[i] = a[i] - k
print(a)
