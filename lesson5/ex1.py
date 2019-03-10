# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

DIR_PRF = 'dir_'


def create_dir(name):
    try:
        os.mkdir(name)
    except OSError as e:
        print(f'Создать директорию {name} не удалось ')
    else:
        print(f'Успешно создана директория {name}')


def remove_dir(name):
    try:
        os.rmdir(name)
    except OSError as e:
        print(f'Удалить директорию {name} не удалось ')
    else:
        print(f'Успешно удалена директория {name}')


def create_dirs():
    [create_dir(DIR_PRF + str(i)) for i in range(1, 10)]


def remove_dirs():
    [remove_dir(DIR_PRF + str(i)) for i in range(1, 10)]


def show_dirs_from_cur():
    print([i for i in os.listdir() if os.path.isdir(i)])


def copy_cur_script():
    script = sys.argv[0]
    shutil.copy(script, script + ".copy")


# create_dirs()
# remove_dirs()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# show_dirs_from_cur()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

#copy_cur_script()