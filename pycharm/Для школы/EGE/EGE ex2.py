numbers = []
n = int(input('Введите длинну массива: '))
for i in range(n):
        numbers.append(int(input()))
summ = 0
for i in range(len(numbers)):
        summ = summ + numbers[i]
scht = 0
if summ%2 == 0:                       #Если сумма всех цифр массива кратно 2
        for i in range(len(numbers)):
            if numbers[i]%2!=0:
                scht+=1
else:                                 #Если сумма всех цифр массива не кратно 2
    for i in range(len(numbers)):
            if numbers[i]%2==0:
                scht+=1
print(scht)
            
