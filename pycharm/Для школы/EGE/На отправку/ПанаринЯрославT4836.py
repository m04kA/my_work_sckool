from random import randint
a = [40, 100, 27, 90, 54]
N = 2018

#for i in range(N):
 #   a.append(int(randint(1, 150)))

k = min(a)

for i in range(len(a)):
    if a[i] > k*2:
        a[i] = a[i] - k*2
print(a)
