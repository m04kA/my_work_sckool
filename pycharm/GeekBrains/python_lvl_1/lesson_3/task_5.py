stop = True
answer = 0
while stop:
    numbs = input().split()
    for el in numbs:
        if el == '*':
            stop = False
        else:
            answer += int(el)
    print(answer)
