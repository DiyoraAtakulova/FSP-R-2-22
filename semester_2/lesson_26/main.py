"""
    python -m venv venv

Это изолированное место с модулями для проекта
"""
# import random
# import sys
# from random import randint
import lesson_26

# print(lesson_26.infinite([0,7], 5))
# print(lesson_26.MAX_TRIES)

import shop_dir.shop as shp

# print(shp.buy([2, 3, 4]))
# print(shop_dir.shop.buy([2, 3, 4]))

from lesson_26 import MAX_TRIES
# print(MAX_TRIES)

# print(__name__)

def main():
    print("Works")

if "__main__" == __name__:
    print(__name__)
    # print("run this")

