
# 2

import random

a = int(input("Input initial range:"))
b = int(input("Input last range:"))
x = random.randint(a, b)

def find_number(x):
    if num == x:
        return True
    else:
        return False


print(f"Вам нужно найти число в диапазоне от {a}-{b} ({x})")

for i in range(3):
    num = int(input("Введите число х: "))
    result = find_number(x)

    if result:
        print("Правильно!")
        break
    else:
        print("Попробуйте еще раз!")