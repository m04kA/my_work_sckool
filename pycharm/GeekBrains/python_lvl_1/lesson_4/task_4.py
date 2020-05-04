first_spisok = [10, 11, 17, 52, 17, 0, 88, 10, 6, 0]

answer = [first_spisok[idx] for idx in range(len(first_spisok)) if idx == first_spisok.index(first_spisok[idx])]
print(answer)
