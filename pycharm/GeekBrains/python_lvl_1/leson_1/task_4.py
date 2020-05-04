# number = int(input('Введите ваше число: '))
number = 7801
answer = 0
while number != 0:
    if number % 10 > answer:
        answer = number % 10
    number = (number - number % 10) // 10
print(f'Самая большая цифра в этом числе: {answer}')
