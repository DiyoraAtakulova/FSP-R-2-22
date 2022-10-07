"""
Основы ООП(Объектно Ориентированное Программирование):
    Наследование 
    Полиморфизм - это единый интерфейс для операция над разными типами данных
        +
        2 + 2 = 4
        '2' + '2' = '22'
        [2,3] + [4,5] = [2,3,4,5]
        len("fgd")
    Инкапсуляция - способность изолировать
    Абстракция (просто знать название)

у классов могут существовать свои переменные
переменные класса - это аргументы
функции класса - это методы

Функциональное пограммирование

"""
# def person(a,b,  c):
#     pass

# p = person(1, 2, 3)
# p_2 = person()


# dunder/magic functions __init__
# Названия в классах каждая первая буква с большой буквы
class Person: 
    pi = 3.14
    # _private = "private"
    # __super_secret = "super_secret"

    def __init__(self, name, surname, age): # self это ссылка к методу классу
        self.name = name
        self.surname = surname
        self.age = age
        self._private = "private"
    
    def get_full_name(self):
        return f"My name is {self.name} and my surname {self.surname}"
    
    def multiply(self, a, b):
        return a * b

    def _thoughts(self):
        a = self.get_full_name()
        b = self.multiply(4, 5)
        print(a, "multiply", b)
        # думать

    def do_all(self):
        self._thoughts() 


# инициализировать класс - создать/вызвать
# и создать экземпляр класса
person_1 = Person("Aybek", "Tordaliev", 15)
person_2 = Person("Kim", "Pak", 45)
# print(Person.__super_secret)

print(person_1._private) # так делать не надо

# print(person_1.name, person_1.surname, person_1.age)
# full_name = person_1.get_full_name()
# print(full_name)

# print(person_2.name, person_2.surname, person_2.age)
# print(person_2.get_full_name())

# print(person_1.multiply(12, 120))

# print(dir(Person))
# print(Person.pi, person_1.name)


# print(person_1, person_2, dir(Person))