class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self, something=''):
        print(f'Запуск отрисовки {something}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером.')


my_pen = Pen('Pen')
my_Pencil = Pencil('Pencil')
my_Handle = Handle('Handle')
my_pen.draw()
my_Pencil.draw()
my_Handle.draw()
