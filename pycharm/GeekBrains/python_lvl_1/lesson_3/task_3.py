numbers = ['*', '*', '*']
for idx in range(len(numbers)):
    numbers[idx] = int(input('Введите число: '))


def sum_max(nubs):
    num = max(nubs)
    nubs.remove(num)
    return num + max(nubs)


print(sum_max(numbers))
