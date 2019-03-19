#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Card:
    matrix = [[], []]
    view = [[], []]

    def __init__(self):
        self.__values = []
        while len(self.__values) < 15:
            n = random.randint(1, 99)
            if n not in self.__values:
                self.__values.append(n)
        self.__values.sort()
        self.prepare_view()

    def prepare_view(self):
        self.matrix = [[None for j in range(0, 9)] for i in range(0, 3)]
        groups = [[], [], []]
        for p in enumerate(self.__values):
            index = p[0]
            groups[index % 3].append(index)
        mask = []
        for i in range(3):
            m = []
            while len(m) < 5:
                n = random.randint(0, 9)
                if n not in m:
                    m.append(n)
            m.sort()
            mask.append(m)
        # print(groups)
        # print(mask)
        self.view = self.matrix.copy()
        for j in range(3):
            for i in range(9):
                if i in mask[j]:
                    self.view[j][i] = groups[j][mask[j].index(i)]

        # print(self.view)

    def show(self):
        print('-' * 40)
        for j in range(3):
            s = ""
            for i in range(9):
                v = ' ' if self.view[j][i] == None else self.__values[self.view[j][i]]
                s += f'{str(v).replace("-1", "-").rjust(4)}'
            print(s)
        print('-' * 40)
        print("")
        # print(self.__values)

    def is_exist(self, number):
        index = -1
        if number in self.__values:
            index = self.__values.index(number)
        return index

    def check(self, number):
        i = self.is_exist(number)
        if number in self.__values:
            index = self.__values.index(number)
            self.__values[index] = -1
            return True
        return False

    def check_win(self):
        for i in range(0, 15):
            if self.__values[i] != -1:
                return False
        return True


class Box():
    i = 0

    def __init__(self):
        self.__numbers = [i for i in range(1, 100)]
        random.shuffle(self.__numbers)
        # print(self.__numbers)
        # print(len(self.__numbers))

    def next(self):
        result = -1
        if 0 <= self.i < len(self.__numbers):
            result = self.__numbers[self.i]
            self.i += 1
        print()
        print(f'Attention! number : {result}. There are {len(self.__numbers[self.i:])}')
        return result

    def show(self):
        print(len(self.__numbers[self.i:]), self.__numbers[self.i:])


class Player:
    isAutomode = False
    name = "player"

    def __init__(self, name, isAutoMode):
        self.name = name
        self.isAutoMode = isAutoMode

    def set_new_card(self):
        self.card = Card()
        print(f'{self.name}, set card for you:')
        self.card.show()

    def ask(self, number):
        print(f'{self.name}, do you have this number: {number}?  y/n')
        answer = self.get_answer(number)
        if answer == 'y':
            if self.card.is_exist(number) >= 0:
                self.card.check(number)
                print(f'{self.name}, you are right!')
                return 3 if self.card.check_win() else 1
            else:
                print(f'{self.name}, wrong answer. There  is no this number')
                return 2
        else:
            if self.card.is_exist(number) >= 0:
                print(f'{self.name}, wrong answer. Your card has this number!')
                return 2
            else:
                print(f'{self.name}, you are right!')
                return 1

    def get_answer(self, number):
        if (self.isAutoMode):
            return 'y' if self.card.is_exist(number) >= 0 else 'n'
        else:
            return input("Your answer: ")


class Game:
    players = []
    cur_player_index = 0

    def __init__(self):
        self.players.append(Player("Person", True))
        self.players.append(Player("Robot", True))
        # self.players.append(Player("Robot", False))
        self.box = Box()
        [p.set_new_card() for p in self.players]

    def play(self):

        is_finish = False
        s = 1

        while not is_finish:
            print(f'Step № {s}')
            number = self.box.next()

            for p in self.players:
                res = p.ask(number)
                if res == 1:
                    pass
                elif res == 2:
                    is_finish = True
                    print(f'{p.name}, you lost!')
                    break
                elif res == 3:
                    is_finish = True
                    print(f'{p.name}, you win!')
                    break

            [p.card.show() for p in self.players]
            s += 1


game = Game()
game.play()