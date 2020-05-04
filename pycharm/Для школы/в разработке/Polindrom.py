
numb = input()
for i in range(len(numb)//2):
    if numb[i] != numb[len(numb)-1-i]:
        score = 1
        break
    else:
        score = 0
if score == 1:
    print('Число не полиндром')
else:
    print('Число полиндром')

        

