
# import sys
# import random

# a = int(input("Input initial range:"))
# b = int(input("Input last range:"))
# x = random.randint(a, b)

# def find_number(x):
#     if num == x:
#         return True
#     else:
#         return False


# print(f"Вам нужно найти число в диапазоне от {a}-{b} {x}")
# while True:
#     num = int(input("Введите число х: "))
#     result = find_number(x)
#     if result:
#         print("Правильно!")
#         break
#     else:
#         print("Попробуйте еще раз!")


# Overloading - перегружение
class Player:
    def __init__(self, x):
        self.x = x

    @classmethod
    def overload_init(cls, x):
        return cls(x*2)

     # cls вызывает класс
    # classmethod позволяет перезаписывать существующий класс __init__

    # def __str__(self):
    #     return f"Класс с аргументом х={self.x}"

    def __repr__(self):
        return f"x={self.x!r}" 

player_1 = Player("12")
player_2 = Player.overload_init(23)

# print(player_1.overload_init(32))
print(player_1)
# print(player_2.x)

# import datetime
# date = datetime.datetime(2012, 12, 12,3, 20, 20) #год/месяц/день/часы/ и тд
# print(str(date), repr(date), sep="\n")
