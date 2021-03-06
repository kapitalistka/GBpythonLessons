# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

employers = ['vasya', 'petya', 'kolya', 'jenya', 'sasha']
salaries = [65000, 20000, 15000, 140000, 25000]

with open("salary.txt", 'w', encoding='utf-8') as file:
    for k, v in dict(zip(employers, salaries)).items():
        file.write(f'{k} - {v}\n')


def do_tax(data):
    return (data[0], int(data[1]) * 0.87)


with open("salary.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    records = dict(map(lambda l: l.strip().split(" - "), lines))
    taxed_records = dict(map(do_tax, records.items()))
    filtered = list(filter(lambda item: int(item[1]) <= 50000, taxed_records.items()))
    # print(taxed_records)
    print(*filtered, sep='\n')
