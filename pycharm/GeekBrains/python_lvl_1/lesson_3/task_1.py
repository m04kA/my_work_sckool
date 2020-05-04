num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))


def division(numerator, denominator):
    if denominator == 0:
        print('Вы хотите разделить на 0!')
    else:
        return  numerator / denominator


print(division(numerator=num_1, denominator=num_2))

# Решение через обработку исключения:
# def division(numerator, denominator):
#     try:
#         print(f'{numerator} / {denominator} = {(numerator / denominator)}')
#
#     except ZeroDivisionError():
#         print('Вы хотите разделить на 0!')
