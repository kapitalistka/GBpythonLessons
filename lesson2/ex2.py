# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
list = [2, -5, 8, 9, -25, 25, 4]
new_list = []

for el in list:
    a = pow(el, 0.5)
    if el >= 0 and a.is_integer():
        new_list.append(int(a))
print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days = ['',
        'первое',
        'второе',
        'третье',
        'четвертое',
        'пятое',
        'шестое',
        'седьмое',
        'восьмое',
        'девятое',
        'десятое',
        'одиннадцатое',
        'двенадцатое',
        'тренадцатое',
        'четырнадцатое',
        'пятнадцатое',
        'шестнадцатое',
        'семьнадцатое',
        'восемьнадцатое',
        'девятнадцатое',
        'двадцатое',
        'двадцать первое',
        'двадцать второе',
        'двадцать третье',
        'двадцать четвертое',
        'двадцать пятое',
        'двадцать шестое',
        'двадцать седьмое',
        'двадцать восьмое',
        'двадцать девятое',
        'тридцатое',
        'тридцать первое']

month = ['',
         'января',
         'февраля',
         'марта',
         'апреля',
         'мая',
         'июня',
         'июля',
         'августа',
         'сентября',
         'октября',
         'ноября',
         'декабря']

str = '02.11.2013'
da = str.split('.')
print(f'{days[int(da[0])]} {month[int(da[1])]}  {int(da[2])} года ')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

n = 5
l = []
for i in range(0, n):
    l.append(random.randint(-100, 100))
print(l)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst1 = []
lst2 = []

for e in lst:
    count = lst.count(e)
    if lst1.count(e) < 1:
        lst1.append(e)
    if lst.count(e) == 1:
        lst2.append(e)

print(lst1)
print(lst2)