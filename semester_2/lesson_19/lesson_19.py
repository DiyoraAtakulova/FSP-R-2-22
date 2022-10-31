# повтор:
# class Player:
#     name = "player"

# class PlayerFather:
#     name = "player_father"

# class PlayerSon(Player, PlayerFather):
#     pass

# player_1 = Player()
# print(PlayerSon.mro())
# print(player_1.name)

"""
Functional Programming
What is Functional Programming
Pure Finctions
map()
filter()
zip()
reduce()
lambda expressions
List Comprehensions
Set and Dictionary Comprehensions
"""

# print(str([231])[3])
# print(list((2,3,4)))

# map(func, *iterables)
# Make an iterator that computes the function using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted. 

def multiply(x):
    return x * 2

result = list(map(multiply, [2, 3, 4]))
print(type(result), result)

# Короткая запись True False
result = True if 1 == 1 else False
print(result)

def check_even(x): # 3 None 
    return True if x % 2 == 0 else False
    # if x % 2 == 0:
    #     return True

result = list(filter(check_even, [2, 3, 4, 5, 6]))
print(result)

# zip(*iterables)
zipper = zip([2, 3, 4, 5], (5, 6, 7), {3, 5, 6, 7})
print(list(zipper))

def func(a, d="sad", *args, user="fgf", game, **kwargs):
    pass

# Написать функцию, которая принимает любой формат аргументов
def finc(*args, **kwargs):
    return args, kwargs

func = finc(1,2,3,4, [234,531], {1:"dadsd"}, sde = "ghgjd", rasge = "100")
print("Func",func)

def any_args(*args):
    print(args)

any_args(2, 3, [5, 6])


class CopyList(list):
    pass

l = CopyList()
l.append(300)
print(l)
r = []
r.append(2)
print(r)

