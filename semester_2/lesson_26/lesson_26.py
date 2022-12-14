"""
3. Создайте функцию infinite(lst, tries), которая будет проходиться 
    по элементам списка lst (целые числа) заданное количество раз (tries) циклически.  
    Один раз - один элемент списка.  
    После вывода последнего значения последовательности процедура начнется с самого начала. 
"""
MAX_TRIES = 100

def infinite(lst, iterations):
    result = ''
    iter_lst = iter(lst) # [0, 7] iterator -> next
    if lst:
        for i in range(iterations):
            try:
                result += str(next(iter_lst))
            except StopIteration:
                iter_lst = iter(lst)
                result += str(next(iter_lst))
    return result

print(infinite([0, 7], 6))

# print(__name__)

if "__main__" == __name__:
    print(__name__)
    print("run this")
