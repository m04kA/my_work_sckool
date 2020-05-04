kratn = 120  # Кратное число
my_arr = [0] * kratn # Мы создаём таблицу максимальных элементов (их индекс - это их остаток от деления на 120)

first_num = 0  # 2-el суммы
second_num = 0  # 2-el суммы
n = int(input())  # Количество эллементов

for el in range(n):  # Поиск суммы с числами, уже пройденными и заполнение таблицы остатков наибольшим числом. Проходясь таким циклом схраняется условие i < j
    new_el = int(input())
    remains = new_el % kratn  # Поиск остатка для дальнейшего заполнения таблицы и поиска этому числу пары
    if my_arr[(kratn - remains) % kratn] > new_el and my_arr[(kratn - remains) % kratn] + new_el > first_num + second_num:  # Проверка на то, что предыдущий элемент больше и проверка на наибольшую сумму
        first_num = my_arr[(kratn - remains) % kratn]
        second_num = new_el
    if my_arr[remains] < new_el:  # Перезапись числа с таким же остатком
        my_arr[remains] = new_el

print(first_num, second_num)


