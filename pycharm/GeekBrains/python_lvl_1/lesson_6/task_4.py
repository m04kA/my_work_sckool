class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Едем!')

    def stop(self):
        print('Стоим!')

    def turn(self, direction):
        print(f'Направляеся {direction}')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость!')
        else:
            print(f'Ваша скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость!')
        else:
            print(f'Ваша скорость {self.speed}')


class PoliceCar(Car):
    pass


my_car = SportCar(100, 'red', 'Porshe')
my_car_2 = WorkCar(65, 'red', 'Gip')

my_car.show_speed()
my_car.go()
my_car_2.show_speed()


