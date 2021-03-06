# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ["яблоко", "банан", "киви", "арбуз"]

for f in fruits:
    print(f'{fruits.index(f)}. {f.rjust(10)}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits = ["яблоко", "банан", "киви", "арбуз"]
greens = ["трава", "яблоко", "арбуз", "изумруд"]

for el in greens:
    if el in fruits:
        fruits.remove(el)

print(fruits)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numbers = [2, 34, 4, 67, 3, 7, 9, 1, 6]
new_numbers = []
for n in numbers:
    if n % 2 == 0:
        new_numbers.append(n / 4)
    else:
        new_numbers.append(n * 2)

print(new_numbers)
