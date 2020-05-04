s = 6
arr = [0] * s

n = int(input())  # Кол. эл.

for i in range(s):
    arr[i] = int(input())

score = 0  # Пары
numb_3 = 0
numb_2 = 0
numb_6 = 0

for i in range(s, n):
    k = i % s
    if arr[k] % 6 == 0:
        numb_6 += 1
    elif arr[k] % 3 == 0:
        numb_3 += 1
    elif arr[k] % 2 == 0:
        numb_2 += 1
    dop = int(input())
    if dop % 6 == 0:
        score = score + i - s + 1
    elif dop % 3 == 0:
        score = score + numb_2 + numb_6
    elif dop % 2 == 0:
        score = score + numb_3 + numb_6
    arr[k] = dop

print(score)