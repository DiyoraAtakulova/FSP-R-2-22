
"""
Дз
1. Исправить ошибки в коде. 
    map_result = list(map(lambda : x, my_floats)) 
    filter_result = list(filter(lambda name: name, my_names, my_names)) 
    reduce_result = reduce(lambda num1, num2: num2, my_numbers, 0)
2. Сортировака списка используя sort по второму значению внутри кортежа 
    a = [(2,4), (0, 2), (2 ,-2), (5, 4)]
3. Написать программу которая принимает начальные и конечные числа диапазона. 
    Используя их и randint,  
    найти рандом число и написать программу, которая, принимает ввод пользователя, 
    до тех пор пока он число не нашёл число из randint 
 
Доп: Если человек который находит число, введет его 3 раза неправильно,
    закончить программу и  вывести сообщение
"""

# 1
from functools import reduce
import math

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59] 

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"] 

my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: math.ceil(x**2), my_floats)) 
print("MAP_RESULT",map_result)

filter_result = list(filter(lambda name: len(name)>7, my_names)) 
print("FILTER_RESULT",filter_result)

reduce_result = reduce(lambda num2, my_numbers: num2 + my_numbers, my_numbers)
print("REDUCE_RESULT",reduce_result)


# 2 
a = [(2,4), (0, 2), (2 ,-2), (5, 4)]
print(sorted(a, key=lambda x: x[1]))

# 3
# import random

# # def random_check(*args):


# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# # r_num = random.randint(a, b)
# # print(r_num)
# c = int(input("Check your number:"))

# for i in range(10):
#     if c != random.randint(a, b):
#         c = int(input("Check your number:"))
#         break
#     # else:
#     #     print("yeap")