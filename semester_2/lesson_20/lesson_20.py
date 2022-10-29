
from functools import reduce

nums = [2,3,4]

# def custom_sum(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(custom_sum(nums))

def multiply(x):
    return x*2


result = list(map(multiply, [2,3,4]))
print(result)

def custom_sum(initial, num): # initial условная переменная, initial=0, num=2,3,4
    print(initial, num)
    return initial + num # initial  это как sum+=num, initial=2,5,9 

print("reduce", reduce(custom_sum, nums, 2))
# если не указывать третье значение, то оно равно 0 либо 1 (собственный аргумент)



"""
1. Использовать map и вывести квадрат всех этих чисел округленных в целое число. 
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59] 
2. Исползуя filter вывеси только имена, длина которых больше 7-ми 
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"] 
3. Использовать reduce чтобы вывести сумму этих чисел 
my_numbers = [4, 6, 9, 23, 5]
"""

# 1
import math
def kvadrat(x):
    return math.ceil(x ** 2)

my_floats = list(map(kvadrat, [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]))
print("map", my_floats)

# 2
def func_name(name):
    if len(name) > 7:
        return name

my_names = list(filter(func_name, ["olumide", "akinremi", "josiah", "temidayo", "omoseun"] ))
print("filter", my_names)

# 3
def sum(initial, num):
    return initial + num
my_numbers = reduce(sum, [4, 6, 9, 23, 5])
print("reduce", my_numbers)


result = list(map(lambda x: math.ceil(x ** 2), [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]))
print("lambda result", result)

result = list(filter(lambda name: len(name) > 7, ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]))
print("lambda filter", result)

result = reduce(lambda initial,num: initial + num, [4, 6, 9, 23, 5])
print("lambda reduce", result)


"""
Comprehensions
list - [i for i in iterable]
set = {i for i in iterable}
dict - {key: val for key, val in iterable}
"""
# l = [i for i in range(0, 10, 2)] # list
# print(l, type(l))

# t = (i for i in range(0, 10, 2)) # generator object
# print(t, type(t))

# t = tuple(i for i in range(0, 10, 2)) # tuple
# print(t, type(t))

# s = {i: "val" for i in range(0, 10, 2)}  # set
# print(s, type(s))

# s = {i: "val" for i in [("name", "behruz"), ("name", "abd"), ("name", "jamshid")]}  # set
# print(s, type(s))

"""IMPORT TIME"""
# import time
# start = time.time()
# l = []
# for i in range(0, 900000, 2):
#     l.append(i)
# end = time.time()
# print(end - start)

# start = time.time()
# l = [i for i in range(0, 900000, 2)] # list
# # print(l, type(l))
# end = time.time()
# print("comp", end - start)

# start = time.time()
# t = (i for i in range(0, 9000000, 2)) # generator object
# end = time.time()
# print("gen", end - start)



list_3 = [x*2 for x in range(100) if x % 2 == 0]
print(list_3)

list_3 = [x*2 if x % 2 == 0 else x for x in range(100)]
print(list_3)

a = [(2,4), (0, 2), (2 ,-2), (5, 4)]
a.sort() # сортирует по первому значению 
print(a)

import random
print(random.randint(10, 100))

# ДЗ
#  Написать функцию которая принимает начальные и конечные числа диапазона. 
# Используя их и Randint, найти рандомное число 
# и написать программу, которая принимает ввод пользователя, до тех пор
# пока он число не нашел число из randint

# ДОП: если человек который находит число, введет его 3 раза неправильно,
# закончить программу и вывести сообщение
