my_list = [7, 5, 3, 3, 2]
numb = int(input('Введите число: '))

if numb in my_list:
    print(my_list)
    my_list.insert(my_list.index(numb), numb)
    print(my_list)
else:
    print(my_list)
    for figure in my_list:
        if numb > figure:
            my_list.insert(my_list.index(figure), numb)
            break
        elif figure == my_list[len(my_list) - 1] and numb < figure:
            my_list.append(numb)
    print(my_list)
