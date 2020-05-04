
fraza = input('Введите вашу фразу: ').split()
#fraza = 'вот пример шифра вертикальной перестановки'.split()
fraza = ''.join(fraza)
tabl = []  # Таблица, где будут разделение по ячейкам
col = int(input('Введите кол. столбиков: '))  # Столбики (кол. символов в 1-й строке)
row = int(input('Введите кол. строк: '))  # Строки
cols = []


def print_tabl(tabl):
    for n in tabl:
        print(' '.join(n))


for i in range(row):
    tabl.append(['*'] * col)  # Создание и заполнение пустышками таблицу

# print_tabl(tabl)
# print('  ')
g = 0  # Переменная для заполнения символами табл
for k in range(row):  # Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (len(fraza) - 1):
            break
        if fraza[g] == ' ':  # Проверка и пропуск пробела
            g += 1
        # print('Строчка'+str(k), 'СТолбик'+str(j), 'Символ фразы'+str(g), 'Длинна фразы'+str((len(fraza)) - 1)) #Для отладки работы программы
        tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
        g += 1
print_tabl(tabl)
print('   ')

g = 0
for k in range(row):  # Переходим на следующую строчку
    for j in range(col):  # Заполняем строчку
        if g > (len(fraza) - 1):
            tabl[k][j] = ''  # Удаляем лишние ячейки для вывода шифра
        g += 1

print('  ')
ansv = ''

a = [5, 1, 4, 7, 2, 6, 3]  # Список рандомных индексов для списка индексов столбцов
for i in range(col):  # Заолнение массива кол.
    cols.append(i)  # Массив индексов столбцов
    # Список рандомных индексов для списка индексов столбцов

# random.shuffle(a)    #Перемешивание для рандомного выведения по столбцам


counter = 0  # Индекс для рандомных индексов для индексов столбиков

for k in range(col):

    for j in range(row):
        for i in range(len(a)):
            if a[i] - 1 == k:
                index = i
        ansv = ansv + str(tabl[j][index])  # cols[a[i]-1]

    counter += 1  # Переход на следующий рандомный индекс индексов столбиков

print(ansv)
