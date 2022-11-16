
# try:
#     # code
#     a = 1/0
# except Exception as err:
#     print(err)


# # class A:
# #     pass

# # print(Exception.mro())

# class WrongInputError(Exception):
#     """Происходит во время ввода чисел"""

# name = input()
# if "l" in name:
#     raise WrongInputError

"""
iterable - исчесляемые переменные или переменные которые
выдают вам значение при последовательном вызове
iterator
iter
next
generator

- как понять что переменная является iterable?
    является исчесляемой
    поддерживает метод __iter__ и next

"""

def make_list(num):
    result = []
    for i in range(num):
        result.append(i+2)
    return result

# my_list = make_list(1000)
# print(my_list)

gen = (x for x in range(5))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
print("works")

# print(type(range(10))) # tuple, list
# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i)

# itr = iter(l)
# print(itr)
# val = next(itr)
# print(val)

# def a():
#     next(itr)
# a()

# print(next(itr))
# print(next(itr))
# print(next(itr))


def generator_func(num):
    for i in range(num):
        yield i+2 # 0+2=2; 
        print("func")

# yield - останавливает функцию помле вызова, пока вызов не произойдет снова

g = generator_func(100)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in generator_func(10):
#     print(i)

from time import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"{t2-t1}s time passed")
    return wrap_func

@performance
def long_time():
    print("2")
    for i in list(range(1000000)):
        i*2

@performance
def long_time_2():
    print("2")
    for i in list(range(1000000)):
        i*2

# long_time()
# long_time_2()


class MyGen:
    current = 0
    def __init__(self, first, last, step=1):
        self.first = first
        self.last = last
        self.step = step

    def __iter__(self):
        return self # self это ссылка на класс MyGen

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += self.step
            return num # 1
        raise StopIteration

iter
next
gen = MyGen(0, 5)
# for i in gen: # iter -> next
#     print(i)


def fibb_list(number):
    a, b = 0, 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

# print(fibb_list(10))

# print(range(100))
# print(list(range(100)))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i + 2)
    return result

# my_list = make_list(100)
# print(my_list)

