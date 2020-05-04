class Organism:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, row):
        answ = ''
        for _ in range(0, self.cell // row, 1):
            answ += '*' * row + '\n'
        for _ in range(0, self.cell % row, 1):
            answ += '*'
        return answ

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Organism(self.cell + other.cell)

    def __sub__(self, other):
        return Organism(self.cell - other.cell)

    def __mul__(self, other):
        return Organism(self.cell * other.cell)

    def __truediv__(self, other):
        return Organism(self.cell // other.cell)


my_org = Organism(20)
print(my_org.make_order(6))
