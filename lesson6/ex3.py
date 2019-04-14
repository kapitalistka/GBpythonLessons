# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy():
    color = ''
    type = ''

    def __init__(self):
        self.name = "Toy"

    def set_name(self, name):
        self.name = name

    def set_color(self, c):
        self.color = c

    def set_type(self, t):
        self.type = t

    def info(self):
        print(__dict__)


class AnimalToy(Toy):

    def __init__(self):
        super().__init__()
        self.type = "животное"

    def set_type(self, t):
        pass


class MultyHeroToy(Toy):

    def __init__(self):
        super().__init__()
        self.type = "персонаж"

    def set_type(self, t):
        pass


class ToyFactory():

    def makeToy(self, name, color, type):
        toy = Toy()
        if type == 'животное':
            toy = AnimalToy()
        elif type == "персонаж":
            toy = MultyHeroToy()
        toy.set_name(name)
        toy.set_color(color)
        toy.set_type(type)
        self.buy_row()
        self.tailor()
        self.color()
        print(f"получился: {toy.type} {toy.color} {toy.name}")
        return toy

    def buy_row(self):
        print("закупили материал...")

    def tailor(self):
        print("пошили...")

    def color(self):
        print("покрасили..")


factory = ToyFactory()
toy1 = factory.makeToy("слоник", "зеленый", "животное")
toy2 = factory.makeToy("маша", "розовая", "персонаж")
toy3 = factory.makeToy("абракадабра", "серая", "что-то непонятное")
