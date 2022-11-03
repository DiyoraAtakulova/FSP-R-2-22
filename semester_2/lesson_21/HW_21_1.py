# 1 не получилось

import sys
import random

# a = int(input("Input initial range:"))
# b = int(input("Input last range:"))

# user_input = sys.stdin
# print("Input : ", user_input)

# x = random.randint(a, b)

class Num:

    def sys_func(numbers):
        numbers = random.randint(sys.stdin)
        # print()

    def find_number(x):
        if num == x:
            return True
        else:
            return False


print(f"Вам нужно найти число в диапазоне")
while True:
    num = int(input("Введите число х: "))
    result = Num.find_number(x)
    if result:
        print("Правильно!")
        break
    else:
        print("Попробуйте еще раз!")