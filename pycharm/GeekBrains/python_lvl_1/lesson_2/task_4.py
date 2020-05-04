# fraz = input('Ввежите ваши слова: ').split()
fraz = '12345678901111 hello my world'.split()
for idx, word in enumerate(fraz, 1):
    if len(word) > 10:
        print(idx, word[:10])
    else:
        print(idx, word)
