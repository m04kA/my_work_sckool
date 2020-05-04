a = [1, 2, 3, 4, 5]

for idx in range(0, len(a) if len(a) % 2 == 0 else len(a) - 1, 2):
    a[idx], a[idx + 1] = a[idx + 1], a[idx]
print(a)
