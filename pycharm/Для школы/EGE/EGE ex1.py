num = input('Введите число: ')
n = []
for i in num:
    n.append(int(i)) #Заполняем список цифрами(разбили введённое число)
minn = 10**9
for i in range(len(n)):
    if n[i]%2==0 and minn > n[i]: #Проверяем каждую цифру на чётность и сохраняем минимальную
        minn = n[i]
if minn == 10**9 or int(num) > 10**9:  #Проверка числа по данному в задании условию
    print('NO')
else:
    print(minn)    #Ответ
    
