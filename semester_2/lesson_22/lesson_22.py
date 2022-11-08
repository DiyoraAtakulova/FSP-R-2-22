
# import sys
# import random

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# lifes = 3

# x = random.randint(a, b)
# print(sys.argv)
# def find_number(x):
#     if num == x:
#         return True
#     else:
#         return False

# print(f"Вам нужно найти число в диапазоне {a}-{b}  {x}")
# while True:
#     num = int(input("Введите число х: "))
#     result = find_number(x)
#     if result:
#         print("Правильно!")
#         break
#     elif lifes == 1:
#         print("Жизни закончились")
#         break
#     else:
#         lifes -= 1
#         print("Попробуйте еще раз!")


# def hello():
#     print("hello world")

# class Player:
#     pass

# print(type(hello))
# print(type({1:1}))
# print(type(set()))
# print(type(2.3))
# print(type(1))
# print(type(" "))
# print(type([]))
# print(type(()))
# print(type(Player()))
# print(type)

# hi = hello
# print(hi()) 

"""
Функции высших порядков - это такие функции, которые могут принимать
в качестве аргументов функцию и возвращать другие функции.
это:

map(lambda x: x**2, [2, 3, 4, 5])
filter()
reduce() 

"""

# функции принимает как параметр другую функцию
def hello2(func):
    func()
    return 2

def greeting():
    print("ay")

# hello2(max)

# x = hello2(greeting) # None
# print(x)

# LEGB
# Local Enclosed Global Built-in
# Вызов функции внутри другой функции
name = "Name" # global

def wrapper():
    def hello_world():
        return "Hello World"
    return hello_world() # Hello World

print(wrapper())
# print(name)

"""
    Decorators - это функции, используемые для расширения возможностей
    простых функций, без изменения кода функции.
    Они создаются как простые функции, но в качестве аргумента
    принимают другие функции и добавляют к ним новые возможности.

    Декораторы вызывают с помощью ключевого символа: @имя_функции_декоратора
"""
def my_dec(func):
    def wrapper():
        print("расширяем функционал")
        func()
        print("расширяем функционал")
    return wrapper

# def hello():
#     print("hello")

# print(my_dec(hello)())

# result = my_dec(hello)
# result()

def my_dec(func):
    def wrap_func():
        print("Расширяем Функционал")
        func()
        print("Расширяем Функционал")
    return wrap_func

@my_dec
def hello():
    print("hello")

hello()
# @my_dec
# def bye():
#     print("byee")

# hello()
# bye()
