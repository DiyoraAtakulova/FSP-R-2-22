"""
Вопросы
    ТЕОРИЯ
1. Назовате все базовые типы переменных и их особенности
1. Все базовые типы переменных делятся на изменяемые(set, list, dict) и неизменяемые(int, floor, str, bool, tuple, complex, None). 
    Особенность set={ }: он может содержать разные типы и не иметь дупликатов, также как и индексов и ключей.
    Особенность list=[ ]: имеет индексы и возможны изменения (удаление-pop(), clear (), remove(), добавление-append()), 
    позволяет объединять списки и сортировать.
    Особенность dict={ }: это ключи и и значения, и их возвращения, 
    возможно также удаление и в целом изменение keys,value.
    В int, floor, complex особенность содержать в себе численные значения.
    Особенность str: форматирование строк, индексация, замена, разделение, объединение в кортеж или список.

2. Какие типы переменных можно хранить в качестве значений множества и ключа словаря
2. В качестве значений множества абсолютно любые переменные. В качестве ключа словаря неизменяемые типы.

3. Что такое MRO И наследование в питоне
3. MRO это порядок разрешения методов, то есть описание пути класса, содержащие множественные наследования, можно сказать, линеаризация классов слева направо. 
    Наследование это использование атрибутов и методов из родительского класса(базового класса).


4. Опишите процесс публикования изменений в гитхаб
4. git status -> git add . -> git commit -m "comments" -> git push -> git pull -> git status (для окончательной проверки выложенного репозитория)

5. Что такое декоратор и для чего он нужен?
5. Декораторы - это функции для расширения возможностей функций без изменений кода функции, 
    и в качестве аргумента принимают другие функции, вызываются с помощью @.
"""

"""
    ТЕОРИЯ + ЗАДАЧИ
    1. Перечислите и Приведите пример оператов: сравнения, логических, особые операторы
    1. Операторы сравнения > < >= <= == !=
        Логические операторы and, or, not
        Особые операторы in, not in, is, is not
"""
x = 2
y = 5
print("Comparison operators: ", x > y, x < y, x >= y, x <= y, x == y, x != y)
print("\n""Logical operators: ", x==y and y!=x, x>y or y==y, not(x<y and x==y))
x = '2'
y = '2'
print("\n",x is y, x is not y, x in y, x not in y)

"""
    2. Можно ли вызвать декоратор без @, если да, то приведите пример 
    2. да можно, например так:
"""
def my_dec(func):
    def wrapper():
        print("расширяем функционал")
        func()
        print("расширяем функционал")
    return wrapper

def hello_func():
    print("hello_func")

# hello_func()

"""
    3. Исправьте код. В конце вы должны создать код по проверке данных ползователя
     и возвращает сообщение об успешном или проваленном логине.
"""
def validate(username, password):
    username_prov = "Random"
    password_prov = "2321ewfsef"
    if username_prov == username and password_prov == password:
        return "Вы успешно вошли в систему!"
    else:
        return "Пароль или имя пользователя не правильным"

username= "Random" 
password = "2321ewfsef"
print(validate(username, password))

"""
    4. Приведете список областей видимости в питоне и 
    пример с каждым из них.
    4.  L - local - локальный
        E - enclosed - внутренний
        G - global - глобальный
        B - built-in - встроенный
"""
a = 5
b = 10 # global
def sum(x, y):
    result = x + y # enclosing
    def star():
        print("*" * 3)
        print(result) # local
    star()
    return result
# print(sum(2,2))

"""
    5. Напишите шаблон декоратора который может принимать аргументы
"""
def my_dec(func):
    def function():
        func()
    return function

@my_dec
def hello_func():
    print("hello_func")
hello_func()

"""
    ЗАДАЧИ
    1. Создать функцию генератор по нахождению чисел фиббоначи
"""
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
print(list(fib(10)))

"""
    2.  Создать класс Gum, который описывает жевачку с атрибутами: smell, price, company, name, special_features, count и с методом str, 
        который возвращает информацию о жевачке со всеми атрибутами. 
        От класса Gum создать два других класса: Orbit и Trident. 
        Orbit должен иметь ещё один атрибут country (страна произвдства). 
        Trident должен иметь ещё один атрибут date_of_production (дата производства).

        taste - вкус
        price - цена
        company - производившая компания 
        name - имя 
        special_features - имеет вкус арбуза, лимона и т.д.
        count - количество в упаковке
"""
class Gum(object):
    def __init__(self, smell, price, company, name, special_features, count):
        self.smell = smell
        self.price = int(price)
        self.company = company
        self.name = name
        self.special_features = []
        self.count = int(count)

    class Orbit():
        def country_func(cls, country):
            cls.country = country

    class Trident():
        def date_of_production(cls, date):
            cls.date = date
            
    def method_str(self):
        return self.__init__()

# res = Gum.method_str('')
# print(res)

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def declare_winner(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2
        if self.damage_per_attack > 0:
            if self.health < 0:
                return "error"
            else:
                return f"{self.name_1} attacks {self.name_2}"
        else:
            return "Your damage negative"

# lew = ("Lew", 10, 2)
# harry = ("Harry", 5, 4)
# print(Fighter.declare_winner(lew[0], harry[0]))
