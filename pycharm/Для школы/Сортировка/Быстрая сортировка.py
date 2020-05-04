import time
from random import randint
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3825)

def quickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[len(A)-1]#random.choice(A)
        Left = []
        Middle = []
        Right = []
        for elem in A:
            if elem < q:
                Left.append(elem)
            elif elem > q:
                Right.append(elem)
            else:
                Middle.append(elem)
        return quickSort(Left) + Middle + quickSort(Right)

def create_invert(count):
    my_masive = []
    for idx in range(count, 0, -1):  # заполняем массив рандомными элементами
        my_masive.append(idx)
    return my_masive

count_elemrnts = [el for el in range(1, 3800, 10)]
time_quickSort = []

for el in count_elemrnts:
    first_mas = create_invert(el)
    start = time.time()
    first_mas = quickSort(first_mas)
    time_quickSort.append(time.time() - start)
    print(el)
    print('-----------')
plt.plot(count_elemrnts, time_quickSort, color='green', label='Быстрая')
plt.legend(loc='upper left')
plt.show()
