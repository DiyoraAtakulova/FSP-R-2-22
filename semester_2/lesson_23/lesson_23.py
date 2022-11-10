
# Создать функцию, которая умножает два числа. 
# Создать декоратор, который умножит ответ из функции на два.
# def dec(f):
#     def wrapped(a, b):
#         # f(a, b)
#         return f(a, b) * 2
#     return wrapped

# def func(a, b):
#     return a * b

# res = dec(func)(2, 10)
# print(res)



# def multiply_by_two(func):
#     def wrapped(*args):
#         return func(*args) * 2
#     return wrapped

# @multiply_by_two
# def multiply(a, b):
#     return a * b

# @multiply_by_two
# def get_sum(numbers):
#     return sum(numbers)

# @multiply_by_two
# def get_two():
#     return 2

# print(get_sum([2, 3, 4, 5, 6, 7]))
# print(get_two())
# print(multiply(2, 4))



# def get_sum(numbers, *, lenght):
#     print(lenght)
#     return sum(numbers)

# print(get_sum([2, 3], 2, lenght=3))


import functools

def multiply_by_two(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapped

@multiply_by_two
def multiply(a, b):
    return a * b

print(multiply, multiply.__doc__)

"""
import functools

def decorators(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator"""


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("Behruz") 