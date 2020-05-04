m = []
def funk(num):
    global m
    ext = False
    for idx in range(num):
        m.append(int(input()))
        ext = bool(input())


funk(7)
print(m)