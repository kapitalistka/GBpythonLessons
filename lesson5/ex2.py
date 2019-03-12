# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import lesson5.ex1 as lib
import os


def go_to_dir(dir):
    try:
        os.chdir(dir)
        print(f'Вы успешно перешли в {os.getcwd()}')
    except:
        print(f'Невозможно перейти в {dir}')


def remove_dir(dir):
    try:
        lib.remove_dir(dir)
        print(f'Вы успешно удалили {dir}')
    except:
        print(f'Невозможно удалить {dir}')


def create_dir(dir):
    try:
        lib.create_dir(dir)
        print(f'Вы успешно создали {dir}')
    except:
        print(f'Невозможно создать {dir}')


def process_user_choice(choice):
    if choice == 1:
        go_to_dir(input('Введите имя папки: '))
    elif choice == 2:
        lib.show_dirs_from_cur()
    elif choice == 3:
        remove_dir(input('Введите имя папки: '))
    elif choice == 4:
        create_dir(input('Введите имя папки: '))


while True:
    try:
        choice = int(input('Выберите пункт:\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           '---------------------\n'
                           'Ваш выбор:'))
    except:
        print("Некорректный ввод!")
        continue
    if choice == 5:
        break
    elif choice in range(1, 5):
        process_user_choice(choice)

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
