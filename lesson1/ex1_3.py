# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",

age = int(input("Сколько Вам лет?: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")