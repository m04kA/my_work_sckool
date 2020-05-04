f_open = open("num_3.txt", "r", encoding='utf-8')
lines = f_open.readlines()
staff_min = []
sr_zp = 0
for idx in range(len(lines)):
    lines[idx] = lines[idx].split()
    if int(lines[idx][1]) < 10000:
        staff_min.append(lines[idx][0])
    sr_zp += int(lines[idx][1])
sr_zp /= len(lines)
print(f'Сотрудники имеющие оклад меньше 10 000: {staff_min}')
print(f'Средняя величина дохода сотрудников: {sr_zp}')
f_open.close()