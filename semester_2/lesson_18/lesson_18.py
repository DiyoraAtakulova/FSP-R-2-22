"""
Пройденные материалы:
Создание класса 
Создание атрибутов класса 
 
Полиморфизм 
Наследование 
MRO 
C1 линейный алгоритм 
 
Методы класса 
Как использовать меотды и атрибуты класса внутри самого класса  
 
Наслдование с is_super() 
Как наследовать и использовать атрибуты и методы отцовского(их)  
классов внутри другого класса 
Приватные переменные  
Приватные атрибуты 
 
Основы ООП (Объектно Ориентированное Программирование): 
    Наследование 
    Полиморфизм - это единный интерфейс для операций над разными типами данных 
        + 
        2 + 2 = 4 
        '2' + '2' = '22' 
        [2, 3] + [4, 5] = [2, 3, 4, 5] 
        len("fdf") 
    Инкапсуляция
    Абстракция(для общего понятия)
"""

class Person:
    _secret = [] # _ обозначает приватные переменные, исп-ся внутри класса
    birthday = "birthday"

    # dunder method(magic method)
    def __init__(self, name, age): 
        self.name = name
        self.age = age 

    def get_info(self):
        return f"{self.name} {self._get_age()}"
    
    def _get_age(self):
        return self.age

# print(Person.birthday)
# # инициализация - создание копии/экземпляра
# person_1 = Person("Gibby", 30)


class Calculator:
    """
    Декоратор — это функция, которая 
    позволяет обернуть другую функцию для расширения её функциональности 
    без непосредственного изменения её кода.
    Декораторы пишутся с помощью знака @
    """

    @staticmethod
    def add_number(num1, num2):
        return num1 + num2

# convert add_numvers() to static method

Calculator.add_number = staticmethod(Calculator.add_number)
# внутри статичного метода не используются атрибуты класса

sum = Calculator.add_number(5, 7)
print("Sum =", sum)


from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear): # cls для отличия статик метода от класс метода
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()
