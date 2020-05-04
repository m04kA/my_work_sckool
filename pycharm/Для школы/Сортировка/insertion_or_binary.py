from random import randint


def massive(minim, maxim, count):
    my_masive = []
    for idx in range(count):  # заполняем массив рандомными элементами
        my_masive.append(randint(minim, maxim))
    return my_masive


def insertion(mass):
    for idx_el_compare in range(len(mass)):
        el_in_mass = idx_el_compare - 1
        key_el = mass[idx_el_compare]
        while mass[el_in_mass] > key_el and el_in_mass >= 0:
            mass[el_in_mass + 1] = mass[el_in_mass]
            print(mass)
            el_in_mass -= 1
        mass[el_in_mass + 1] = key_el
    return mass


def insertion_together(mass):
    if len(mass)%2 == 0:
        for k in range(0, len(mass), 2):
            el_1 = k
            el_2 = k+1
            bufer_1 = mass[k]
            bufer_2 = mass[k+1]
            if bufer_1 > bufer_2:
                bufer_2 = mass[k]
                bufer_1 = mass[k+1]
            for i in range(k-1, -1, -1):
                if mass[i] > bufer_2:
                    mass[el_2] = mass[i]
                    #print(mass)
                    el_2 -= 1
                    el_1 -= 1
                elif mass[i] > bufer_1:
                    mass[el_1] = mass[i]
                    #print(mass)
                    el_1 -= 1
                else:
                    break
                #print('--------')
            mass[el_1] = bufer_1
            mass[el_2] = bufer_2
        return mass
    else:
        for k in range(0, len(mass) - 1, 2):
            el_1 = k
            el_2 = k+1
            bufer_1 = mass[k]
            bufer_2 = mass[k+1]
            if bufer_1 > bufer_2:
                bufer_2 = mass[k]
                bufer_1 = mass[k+1]
            for i in range(k-1, -1, -1):
                if mass[i] > bufer_2:
                    mass[el_2] = mass[i]
                    #print(mass)
                    el_2 -= 1
                    el_1 -= 1
                elif mass[i] > bufer_1:
                    mass[el_1] = mass[i]
                    #print(mass)
                    el_1 -= 1
                else:
                    break
                #print('--------')
            mass[el_1] = bufer_1
            mass[el_2] = bufer_2

        el_2 = len(mass) - 1
        for i in range(len(mass)-2, -1, -1):
            if mass[i] > mass[el_2]:
                mass[i], mass[el_2] = mass[el_2], mass[i]
                el_2 -= 1
            else:
                break
        return mass

mas = [7, 4, 2, 5 , 1]  # massive(0, 10, 5)
print(mas)
mas = insertion_together(mas)
print(mas)
