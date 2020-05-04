from random import randint
from functools import reduce

f_open = open("num_5.txt", "w", encoding="utf-8")
numb = [randint(1, 20) for _ in range(5)]
print(numb)
for idx in range(len(numb)):
    f_open.write(str(numb[idx])+' ')
f_open.close()
z_open = open("num_5.txt", "r", encoding="utf-8")
lines = z_open.readlines()
lines = lines[0].split()
for idx in range(len(lines)):
    lines[idx] = int(lines[idx])
print(f'Их сумма: {reduce(lambda first, second: first + second, lines)}')

z_open.close()
