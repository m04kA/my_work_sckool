structure = []
quantity = int(input('Введите кол. товаров: '))

for idx in range(1, quantity + 1, 1):
    my_dict = {'Название': None, 'цена': None, 'количество': None, 'eд': None}
    for key in my_dict.keys():
        val = input(f'Введите {key}: ')
        my_dict.update({key: val})
    structure.append((idx, my_dict))
print('-------------------')
print(structure)

answer = {'Название': [], 'цена': [], 'количество': [], 'eд': []}
for key in answer.keys():
    value = []
    for idx in range(quantity):
        value.append(structure[idx][1][key])
    answer.update({key: value})
print('-------------------')
print(answer)
