f_open = open("num_4_1.txt", "r", encoding="utf-8")
z_open = open("num_4_2.txt", "w", encoding="utf-8")
lines = f_open.readlines()
numbs = ['Один', 'Два', 'Три', 'Четыре']
for idx in range(len(lines)):
    lines[idx] = lines[idx].split()
    lines[idx][0] = numbs[idx]
for idx_1 in range(len(lines)):
    lines[idx_1] = ' '.join(lines[idx_1]) + '\n'

print(lines)
z_open.writelines(lines)
f_open.close()
z_open.close()
