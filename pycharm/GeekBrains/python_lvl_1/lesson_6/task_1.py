import time


class Traffic_lights:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def runing(self):
        my_time = [7, 2, 5]
        position = 0
        for idx in range(3):
            start = time.time()
            while time.time() - start < my_time[position]:
                print(self.__color[position])
                time.sleep(1)
            print('--------------')
            position += 1


my_traffic = Traffic_lights()
my_traffic.runing()
