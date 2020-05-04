class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def calculation(self):
        height = 5  # 5(см) - высота покрытия
        return self._length * self._width * 25 * height


my_road = Road(5000, 20)
print(f'{my_road.calculation()/1000} тонн')
