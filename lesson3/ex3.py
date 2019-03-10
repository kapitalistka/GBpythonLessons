# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

pattern_player = {"health": 100, "damage": 50}


def name_player(name):
    p = pattern_player.copy()
    p["name"] = name
    return p


def attack(p1, p2):
    print(f' Player {p1["name"]} attacks  player {p2["name"]}')
    p2["health"] -= p1["damage"]


player1 = name_player(input("Enter name of the 1st player: "))
player2 = name_player(input("Enter name of the 2st player: "))


# print(player1)
# print(player2)
# attack(player1, player2)
# print(player1)
# print(player2)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def set_armor(player):
    player["armor"] = 1.2


def calc_damage(damage, armor):
    return round(float(damage) / float(armor), 1)


def attack(p1, p2):
    print(f' Player {p1["name"]} attacks  player {p2["name"]}')
    p2["health"] = float(p2["health"]) - calc_damage(p1["damage"], p1["armor"])
    print(p1)
    print(p2)


def check_death(p):
    if p["health"] <= 0:
        print(f'Player {p["name"]} is died!')
    return p["health"] <= 0


def save_player(player):
    with open(player["name"] + ".txt", "w")as file:
        for k, v in player.items():
            file.write(f'{k} - {v} \n')


def retrieve_player(name):
    # todo по хорошему б сделатьпроверку
    with open(name + ".txt", "r")as file:
        lines = file.readlines()
        return dict(map(lambda l: l.strip().split(" - "), lines))


set_armor(player1)
set_armor(player2)
save_player(player1)
save_player(player2)
hero = retrieve_player("hero")
enemy = retrieve_player("enemy")

print(hero)
print(enemy)

player1 = hero
player2 = enemy
winner_name = ""

while True:
    attack(player1, player2)
    if check_death(player2):
        winner_name = player1["name"]
        break
    attack(player2, player1)
    if check_death(player1):
        winner_name = player2["name"]
        break;

print(f'Player {winner_name} is won!')
print('Game over')
