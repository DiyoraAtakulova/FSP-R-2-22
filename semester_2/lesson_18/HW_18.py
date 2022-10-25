
from datetime import date
# не получился
class Person:
    year = date.year

    def __init__(self, age): 
        self.age = age 

    def _get_age(self):
        self.age = date.year - self.age
        return self.age

person_1 = Person(30)
print(person_1._get_age())
