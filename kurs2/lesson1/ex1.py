# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def task1():
    n = input("Input the number: ")
    if len(n) == 3 and n.isdecimal():
        number = int(n)
        a = int(number / 100)
        b = int((number - a * 100) / 10)
        c = number % 10
        print(f'sum is {a + b + c}, composition is {a * b * c}')
    else:
        print("Incorrect input")


# task1()
# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
def task2():
    print(5 | 6) #101 or 110=111(7)
    print(5 & 6) #101 and 110=100(4)
    print(5 >> 2)# /2^2
    print(5 << 2)# *2^2


# task2()


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def task3():
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k}x + {b}')



task3()

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
def is_triangle_exists(a: int, b: int, c: int):
    if a < b + c and b < c + b and c < a + b:
        return True


def task7():
    global a, b, c
    a = int(input("Input the 1st lenth: "))
    b = int(input("Input the 2st lenth: "))
    c = int(input("Input the 3st lenth: "))
    is_exists = is_triangle_exists(a, b, c)
    if is_exists:
        if a == b == c:
            print("equilateral ")
        elif a == b or b == c or a == c:
            print("isosceles")


# task7()


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def is_leap(year: int):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True


def task8():
    year = int(input("Input year: "))
    print("leap" if is_leap(year) else "not leap")


# task8()

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


def mid(a: int, b: int, c: int):
    if a < b < c or c < b < a:
        return b
    elif a < c < b or b < c < a:
        return c
    else:
        return a


def task9():
    global a, b, c
    a = int(input("Input the 1st number: "))
    b = int(input("Input the 2st number: "))
    c = int(input("Input the 3st number: "))
    print(mid(a, b, c))

# task9()

# Примечание. Решите 6 интересных для вас задач из 9. К каждой задаче приложите блок-схему алгоритма, который вы будите использовать.
