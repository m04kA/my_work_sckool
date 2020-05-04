
import random

numb = []
indx = []

for i in range(1, 10):
    numb.append(i)
    indx.append(i)

random.shuffle(indx)

for i in range(4):
    print(numb[indx[i]-1])
