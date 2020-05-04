from functools import reduce

numbers = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda first, second: first * second, numbers))
