f_open = open("num_2.txt", "r")
rows = f_open.readlines()
print(rows)
print(f'Количество строк: {len(rows)}')
for idx in range(len(rows)):
    rows[idx] = rows[idx].split()
    print(f'Количество слов в строке №{idx + 1} = {len(rows[idx])}')
f_open.close()