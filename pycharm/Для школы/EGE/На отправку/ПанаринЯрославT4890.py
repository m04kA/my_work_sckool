from random import randint
a = [30, 99, 27, 90, 66]
N = 2018
k = a[0]
#for i in range(N):
 #   a.append(int(randint(1, 150)))
for i in range(len(a)):
    if a[i]%3 == 0 and a[i] < k:
        k = a[i]

for i in range(len(a)):
    if a[i]%2 == 0:
        a[i] = a[i] - k
print(a)
