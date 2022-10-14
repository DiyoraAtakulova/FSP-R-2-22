# Задача 1. 
print("ЗАДАЧА 1.")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

r1 = Rectangle(10, 5)
r2 = Rectangle(20, 11)

print("r1.width = ", r1.width)
print("r1.height = ", r1.height)
print("r1.get_width() = ", r1.get_width())
print("r1.get_area() = ", r1.get_area())

print("-------------------")

print("r2.width = ", r2.width)
print("r2.height = ", r2.height)
print("r2.get_widht() = ", r2.get_width())
print("r2.get_area() = ", r2.get_area())

class ToyClass:
    def instance_method(self, a_1, a_2, a_3):
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        return 'instance method called', self
    
    def class_method(cls):
        return 'class method called', cls
    
    def static_method():
        return 'static method called'


# Задача 2.
print("ЗАДАЧА 2.")

class Student:
    def __init__(self, name="Ivan", age=18, group_number="10 A"):
        self.name = name
        self.age = age
        self.group_number = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.name + " " + self.group_number

    def set_name_age(self):
        return self.name, self.age, self.group_number

    def set_group_number(self):
        return self.group_number


student_info = Student()
print(student_info.get_name())
print(student_info.get_age())
print(student_info.get_group_number())

student_info_2 = Student("Diyora", 21, "469 Faculty of Medicine")
print(student_info_2.set_name_age())

student_info_3 = Student("Ivan", 18, "11 A")
print(student_info_3.set_group_number())


# Задача 3.
print("ЗАДАЧА 3.")

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

math_operation = Math(5, 5)
print("a + b =", math_operation.addition())
print("a * b =", math_operation.multiplication())
print("a / b =", math_operation.division())
print("a - b =", math_operation.subtraction())


# Задача 4.
print("ЗАДАЧА 4.")

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def first_method(self):
        return "Автомобиль заведен"

    def second_method(self):
        return "Автомобиль заглушен"

    def year_car(self):
        return self.year

    def type_car(self):
        return self.type

    def color_car(self):
        return self.color

about_car = Car("purple", "BMW X5", 2020)
print(about_car.first_method())
print(about_car.second_method())
print(about_car.year_car(), about_car.type_car(), about_car.color_car())