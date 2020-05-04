from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self, name):
        self.name = name
        self.material = None

    @abstractmethod
    def calc_expenditure(self):
        return self.material

    @property
    def show_material(self):
        return f'Вот нужный материал {self.material}'

    def __add__(self, other):
        self.material += other.material
        return self.material


class Сoat(Сlothes):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)
        self.calc_expenditure(self.value)

    def calc_expenditure(self, value=0):
        self.material = (value / 6.5) + 0.5


class Suit(Сlothes):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)
        self.calc_expenditure(self.value)

    def calc_expenditure(self, value=0):
        self.material = (2 * value) + 0.3


my_coat = Сoat('Сoat', 20)
my_suit = Suit('Suit', 30)
print(my_suit.show_material)
print(my_coat.show_material)
print(my_coat + my_suit)
