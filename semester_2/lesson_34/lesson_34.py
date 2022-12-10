# def do_stuff(num):
#     try:
#         return num + 3
#     except TypeError as err:
#         # print(err)
#         # return "wrong input"
#         # raise ValueError(err)
#         raise ValueError(f"You should input integers. Error message: {err}")

# print(do_stuff("adds"))


import random

def find_number(number, answer):
    """Compares two numbers and return bool.
    
    Args:
        number (int): число для проверки.
        answer (int): искомое число.

    Returns:
        bool
    """
    number = int(number)
    if (number) > 0 and number <= 10:
        if answer == number:
            print("You won!")
            return True
    else:
        print("ВВЕДИТЕ ОТВЕТ МЕЖДУ 1-10 :")
        return False

def main():
    print(f"Вам нужно найти числа в диапазон от {0}-{10}")
    answer = random.randint(0, 10) #
    while True:
        try:
            number = int(input("Введите число x: ")) # 10
            if find_number(number, answer):
                break
            else:
                print("Попробуйте еще раз!")
        except ValueError as err:
            print("Введите число")
            continue

if __name__ == "__main__":
    main()
    
