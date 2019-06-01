__author__ = 'Крымов Иван'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

number = input('Введите число: ')
i = 0
while i < len(number):
    print(number[i])
    i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

print('До замены.... Первое число: ', first_number, 'Второе число:', second_number)

tmp = first_number
first_number = second_number
second_number = tmp

print('После замены.... Первое число: ', first_number, 'Второе число:', second_number)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите ваш возраст: '))
if age >= 18:
    print('Доступ разрешен!')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')