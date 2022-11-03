# 1 

import sys
import random

a = int(sys.argv[1])
b = int(sys.argv[2])

x = random.randint(a, b)

def find_number(x):
    if num == x:
        return True
    else:
        return False


print(f"Вам нужно найти число в диапазоне {a}-{b}  {x}")
while True:
    num = int(input("Введите число х: "))
    result = find_number(x)
    if result:
        print("Правильно!")
        break
    else:
        print("Попробуйте еще раз!")