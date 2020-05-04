from random import randint

def merger(mass):
    if len(mass) < 2:
        return mass[:]
    else:
        left_mass = merger(mass[:len(mass)//2])
        right_mass = merger(mass[len(mass)//2:])
        return merger_help(left_mass,right_mass)

def merger_help(left_side, right_side):
    answ = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_side) and right_idx < len(right_side):
        if left_side[left_idx] < right_side[right_idx]:
            answ.append(left_side[left_idx])
            left_idx += 1
        elif left_side[left_idx] > right_side[right_idx]:
            answ.append(right_side[right_idx])
            right_idx += 1
        else:
            answ.append(right_side[right_idx])
            answ.append(left_side[left_idx])
            right_idx += 1
            left_idx += 1
    while left_idx < len(left_side):
        answ.append(left_side[left_idx])
        left_idx += 1
    while right_idx < len(right_side):
        answ.append(right_side[right_idx])
        right_idx += 1
    return answ

def create(minim, maxim, count):
    my_masive = []
    for idx in range(count):  # заполняем массив рандомными элементами
        my_masive.append(randint(minim, maxim))
    return my_masive

a = create(1, 20, 1)
print(a)
a = merger(a)
print(a)
