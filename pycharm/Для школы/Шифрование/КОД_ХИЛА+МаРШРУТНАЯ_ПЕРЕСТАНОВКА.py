alfovit = {'а': 1, 'б': 18, 'в': 11, 'г': 6, 'д': 0, 'е': 15, 'ж': 20, 'з': 5, 'и': 21, 'к': 23,
           'л': 13, 'м': 4, 'н': 16, 'о': 8, 'п': 25, 'р': 24, 'с': 10, 'т': 19, 'у': 26, 'ф': 12,
           'х': 2, 'ц': 28, 'ч': 7, 'ш': 17, 'щ': 22, 'ь': 3, 'ы': 29, 'э': 27, 'ю': 14, 'я': 9}

print('Маршрутная перестановка')
fraza = input('Введите вашу фразу: ').lower().split()
fraza = ''.join(fraza)
# fraza = 'без труда не вынешь рыбку из пруда'  # input('Введите фразу: ').lower().split()
# fraza = fraza.lower().split()


def marshrut_perestan(fraz):

    fraza = fraz
    tabl = []  # Таблица, где будут разделение по ячейкам
    col = int(input('Введите кол. столбиков: '))  # Столбики (кол. символов в 1-й строке)
    row = int(input('Введите кол. строк: '))  # Строки

    def print_tabl(tabl):
        for n in tabl:
            print(' '.join(n))

    def clear_tabl(tabl):
        for i in range(row):
            tabl.append(['O'] * col)  # Создание и заполнение пустышками таблицу

    def test(k, j, g, fraza):
        print('Строчка ' + str(k), 'СТолбик ' + str(j), 'Символ фразы ' + str(g),
              'Длинна фразы ' + str((len(fraza)) - 1))  # Для отладки работы программы

    def surplus(row, col, fraza, tabl):
        g = 0
        for k in range(row):  # Переходим на следующую строчку
            if k % 2 == 0:
                for j in range(col):  # Заполняем строчку
                    if g > (len(fraza) - 1):
                        tabl[k][j] = ''  # Удаляем лишние ячейки для вывода шифра
                    g += 1
            elif k % 2 != 0:
                for j in range(col - 1, -1, -1):
                    if g > (len(fraza) - 1):
                        tabl[k][j] = ''  # Удаляем лишние ячейки для вывода шифра
                    g += 1

    clear_tabl(tabl)

    #print_tabl(tabl)
    print('  ')

    g = 0  # Переменная для заполнения символами табл

    for k in range(row):  # Переходим на следующую строчку
        if k % 2 == 0:
            for j in range(col):  # Заполняем строчку
                if g > (len(fraza) - 1):  # Проверка на конец фразы
                    break
                if fraza[g] == ' ':  # Проверка и пропуск пробела
                    g += 1
                # test(k, j, g, fraza)

                tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
                g += 1


        elif k % 2 != 0:
            for j in range(col - 1, -1, -1):  # Заполняем строчку в обратном порядке
                if g > (len(fraza) - 1):  # Проверка на конец фразы
                    break
                if fraza[g] == ' ':  # Проверка и пропуск пробела
                    g += 1
                # test(k, j, g, fraza)
                tabl[k][j] = fraza[g]  # Основа, заполняюзая таблицу
                g += 1

    print_tabl(tabl)
    # Чистка таблицы
    surplus(row, col, fraza, tabl)

    print('   ')
    ansv = ''
    a = True
    for j in range(col - 1, -1, -1):
        if a == True:
            for k in range(row):
                ansv = ansv + str(tabl[k][j])
            a = False
        else:
            for k in range(row - 1, -1, -1):
                ansv = ansv + str(tabl[k][j])
            a = True
    return ansv


def shifr_matr():
    mtr_a = []
    for i in range(4):
        mtr_a.append([])
        rashod = (input().split())
        for j in range(4):
            mtr_a[i].append(int(rashod[j]))
    return mtr_a


def zacod_matr(fraz):
    mtr_b = []
    for i in range(4):
        mtr_b.append([])
        for j in range(7):
            mtr_b[i].append('*')
    fraz = ''.join(fraz)
    g = 0
    for i in range(7):
        for j in range(4):
            mtr_b[j][i] = int(alfovit[f'{fraz[g]}'])
            g += 1
    return mtr_b


# matrix_b = zacod_matr(fraza)

# matrix_a = [[1, 2, 3, 4],
#            [1, 2, 3, 5],
#            [1, 3, 3, 5],
#            [1, 3, 4, 5]]  # m*n - (m-строки,n-столбцы)

# matrix_b = [[18, 24, 16, 16, 24, 26, 24],
#            [15, 26, 15, 15, 29, 21, 26],
#            [5, 0, 11, 17, 18, 5, 0],
#           [19, 1, 29, 3, 23, 25, 1]]  # k*l - (k-строки, l-столбцы)


def mult_row_col(m_a, m_b, i, j):
    answer = 0
    for k in range(len(m_a[0])):
        answer += m_a[i][k] * m_b[k][j]
    return answer


def multiply(m_a, m_b):
    m = len(m_a)
    n = len(m_a[0])
    k = len(m_b)
    l = len(m_b[0])
    m_res = []
    for i in range(m):
        m_res.append([''] * l)
    for i in range(len(m_res)):
        for j in range(len(m_res[0])):
            m_res[i][j] = mult_row_col(m_a, m_b, i, j) % 30
    return m_res


def print_tabl(tabl):
    for n in tabl:
        print(' '.join(str(n)))


def transformer(matriks):
    m = len(matriks)
    n = len(matriks[0])
    new_matr = []
    for i in range(n):
        new_matr.append([''] * m)
        for j in range(m):
            new_matr[i][j] = matriks[j][i]
    return new_matr


def get_key(slov, value):
    for k, v in slov.items():
        if v == value:
            return k


def answ(noy_answer):
    answer = ''
    for i in range(7):
        for j in range(4):
            answer += str(get_key(alfovit, noy_answer[j][i]))
    return answer


fraza = 'привет'#marshrut_perestan(fraza)
print(f'Закодированная фраза маошрутной перестановки: {fraza}')
print('Введите матрицу кодировки')
matrix_b = zacod_matr(fraza)
matrix_a = shifr_matr()
print('------------')
print('Матрица закодированной фразы: ')
print_tabl(matrix_b)

cod_matr = multiply(matrix_a, matrix_b)

print('------------')
print('Перемноженная матрица: ')
print_tabl(cod_matr)

#new = transformer(matrix_a)
answer = answ(cod_matr)

# print_tabl(answer)
#print(alfovit['а'])
#print('---------')
#print(fraza)
print('---------')

print(answer)
