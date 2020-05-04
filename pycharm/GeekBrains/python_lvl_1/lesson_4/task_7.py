# Решение №1
# my_num = int(input('Введите крайнее число: '))
my_num = 16
numbs = (el for el in range(1, my_num))
answer = []

result = 1
for el in numbs:
    result *= el
    print(result)
print('----------------')


def my_gener(mux_num):
    for el in range(1, mux_num + 1):
        yield el


result = 1
for el in my_gener(15):
    result *= el
    print(result)
