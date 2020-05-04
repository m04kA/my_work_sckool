class Matrix:
    def __init__(self, matr):
        self.my_matr = matr

    def __str__(self):
        reslt = ''
        for el in self.my_matr:
            for num in el:
                reslt += str(num) + ' '
            reslt += '\n'
        return f'{reslt}'
    def __add__(self, other):
        result = []
        for idx_row in range(len(self.my_matr)):
            result.append([])
            for idx_col in range(len(self.my_matr[idx_row])):
                result[idx_row].append(self.my_matr[idx_row][idx_col] + other.my_matr[idx_row][idx_col])
        return Matrix(result)



matr = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matr + matr_2)
