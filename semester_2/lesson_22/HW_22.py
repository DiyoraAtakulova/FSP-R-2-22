"""
Используя функцию по нахождения факториала, 
написать декортор, который будет запускать его два раза 
и вычислять общее время запуска
"""
from time import time

def do_twice(func):
    def wrapped(n):
        start = time()
        print("result =", func(n))
        # print("result 2 =", func(n))
        end = time()
        print("Время работы = ", end - start)
        # return f"Время работы = {end-start}"
    return wrapped

# @do_twice
def factorial(n):
    if n < 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

result = do_twice(factorial)(10) # return wrapped
# print(result(50))
# print(factorial(3))



