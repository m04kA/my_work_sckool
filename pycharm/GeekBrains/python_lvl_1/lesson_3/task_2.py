first_name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
emaill = input('Ввелите ваш email: ')
numb = input('Введите ваш телефон: ')


def info(first, second, yea, cit, email, num):
    print(f'Имя:{first}; Фамилия:{second}; Год рождения:{yea}; Город:{cit}; Почта:{email}; Номер телефона:{num}.')


info(first=first_name, second=second_name, yea=year, cit=city, email=emaill, num=numb)
