class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.payment = {"wage": wage, "bonus": bonus}
        self._income = sum(map(int,self.payment.values()))


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income


my_people = Position('Yaroslav', 'Panarin', 'programmer', '25000', '5000')
print(my_people.get_full_name())
print(my_people.get_total_income())