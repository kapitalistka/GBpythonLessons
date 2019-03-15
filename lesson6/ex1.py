# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self):
        self.name = "Car"
        self.speed = 100
        self.color = "Black"
        self.is_police = False

    def go(self):
        print(f'{self.name} is going...')

    def stop(self):
        print(f'{self.name} has stopped.')

    def turn(self, direction):
        print(f'{self.name} has turned to the {direction}.')

    def info(self):
        print(self.__dict__)


class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.name = "TownCar"
        self.speed = 60
        self.color = "Grey"


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.name = "SportCar"
        self.speed = 200
        self.color = "Red"


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.name = "WorkCar"
        self.speed = 100
        self.color = "Yellow"


class PoliceCar(SportCar):
    def __init__(self):
        super().__init__()
        self.name = "PoliceCar"
        self.is_police = True


cars = (TownCar(), WorkCar(), SportCar(), PoliceCar())

[c.info() for c in cars]
[c.go() for c in cars]
