s = 3 # Отступ между эллементами
arr = [0] * s #Наши элементы

n = int(input())  # Кол. эл.

for i in range(s):
    arr[i] = int(input())

score = 0  # Пары
numb_24 = 0
numb_12 = 0
numb_8 = 0
numb_6 = 0
numb_4 = 0
numb_3 = 0
numb_2 = 0

for i in range(s, n):
    k = i % s
    if arr[k] % 24 == 0:
        numb_24 += 1
    if arr[k] % 12 == 0:
        numb_12 += 1
    if arr[k] % 8 == 0:
        numb_8 += 1
    if arr[k] % 6 == 0:
        numb_6 += 1
    if arr[k] % 4 == 0:
        numb_4 += 1
    if arr[k] % 3 == 0:
        numb_3 += 1
    if arr[k] % 2 == 0:
        numb_2 += 1
    dop = int(input())
    if dop % 24 == 0:
        score = score + i - s + 1
    elif dop % 12 == 0:
        score += numb_2
    elif dop % 8 == 0:
        score += numb_3
    elif dop % 6 == 0:
        score += numb_4
    elif dop % 4 == 0:
        score += numb_6
    elif dop % 3 == 0:
        score += numb_8
    elif dop % 2 == 0:
        score += numb_12
    else:
        score += numb_24
    arr[k] = dop

    # # elif dop % 3 == 0:
    # #     score = score + numb_2 + numb_6
    # # elif dop % 2 == 0:
    # #     score = score + numb_3 + numb_6
    # arr[k] = dop

print(score)