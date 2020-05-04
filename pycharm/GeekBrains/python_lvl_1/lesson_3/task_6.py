def int_func(word):
    word = word[0].upper() + word[1:]
    return word


words = input().split()
for idx, el in enumerate(words):
    words[idx] = int_func(el)

answer = ''
for el in words:
    answer += f'{el} '
print(answer)
