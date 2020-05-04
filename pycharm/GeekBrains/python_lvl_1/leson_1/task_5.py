# revenue = int(input('Введите выручку фирмы: '))
revenue = 10000
# cost = int(input('Введите издержки фирмы: '))
cost = 100
if revenue > cost:
    profit = revenue - cost
    print(f'Вы работаете в прибыль, вот она: {profit}')
    return_on_revenue = profit / revenue
    # peоple = int(input('Введите количество человек: '))
    peоple = 5
    print(f'Прибыль фирмы на 1 человека: {profit / peоple}')
else:
    profit = cost - revenue
    print(f'Вы работаете в убыток, вот он: {profit}')
