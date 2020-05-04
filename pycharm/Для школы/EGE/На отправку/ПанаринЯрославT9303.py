from random import randint
a = [300, 121, 505, 123, 712, 555]
n = 6

k = 999
for i in range(len(a)):
    if a[i]<k and ((a[i]%10 == (a[i]%100)//10) or (a[i]%10 == a[i]//100) or ((a[i]%100)//10 == a[i]//100)):
        k=a[i]
for i in range(len(a)):
    if (a[i]%10 == (a[i]%100)//10) or (a[i]%10 == a[i]//100) or ((a[i]%100)//10 == a[i]//100):
        a[i] = k
    print(a[i])
