season = ['Зима', 'Весна', 'Лето', 'Осень']
dict_seasons = {
    (1, 2, 12): 'Зима',
    (3, 4, 5): 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень'
}
while True:
    month = int(input('Введите месяц: '))
    if month >= 1 and month <= 12:
        # Чрез list
        if month in [1, 2, 12]:
            print(season[0])
        elif month >= 3 and month <= 5:
            print(season[1])
        elif month >= 6 and month <= 8:
            print(season[2])
        else:
            print(season[3])
        # Через dict
        for key, value in dict_seasons.items():
            if month in key:
                print(value)
                exit()
    else:
        print('Вы ввели число больше кол. месяцев!')
