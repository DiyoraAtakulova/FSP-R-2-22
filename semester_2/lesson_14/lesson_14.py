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
    def __init__(self, name, surname, age): # self это ссылка к методу классу
        self.name = name
        self.surname = surname
        self.age = age
    
    def get_full_name(self):
        return f"My name is {self.name} and my surname {self.surname}"


# инициализировать класс - создать/вызвать
# и создать экземпляр класса
person_1 = Person("Aybek", "Tordaliev", 15)
print(person_1.name, person_1.surname, person_1.age)
full_name = person_1.get_full_name()
print(full_name)

person_2 = Person("Kim", "Pak", 45)
print(person_2.name, person_2.surname, person_2.age)
print(person_2.get_full_name())

# print(person_1, person_2, dir(Person))