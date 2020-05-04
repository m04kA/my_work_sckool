first_list = [10, 5, 72, 72, 1, 10, 29]
answer = [first_list[ind] for ind in range(len(first_list)) if first_list[ind] > first_list[ind - 1]]
print(answer)
