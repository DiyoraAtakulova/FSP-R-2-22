"""

"""
try:
    file = open("test.txt") #файл объект каак итератор
    # # print(file.read())
    # print(file.read(10)) # 0-9
    # print(file.read(10)) # 10-19
    # print(file.read(10)) # 20-29
    # contant = file.read()
    # print(contant)
    # #
    # file.seek(10)
    # print(file.read(100))

    # readline
    # readlines
    # print(next(file))
    # print(file.readline())
    # print(file.readline())
    # file.seek(0)
    # print(file.readlines())

    # print(next(file))
    # print(next(file))
    # for row in file:
    #     print(row)
except Exception as err:
    print(err)
finally:
    file.close() #обязательно 

# Contex manager

# file = open("test.txt")
# mode="r"-для чтения
# with open("test.txt", mode="r") as file:
#     for row in file:
#         print(row)

# mode="w"-чоздает и читает новы файл
# with open("test_write.txt", mode="w") as file:
#     file.write("Some random text")
#     file.write("Some random text")
#     file.write("Some random text")

# r - read
# w - write
# a - append
# with open("test_write.txt", mode="a") as file:
#     file.write("\nAnother random text")
    # file.writelines(["\nAnother random text", "Two"]) #принимает список

# mode="x" - для создания текста в новом файле
# with open("test_write_2.txt", mode="x") as file:
#     file.write("\nAnother random text")

# mode="wb" - записывает бинарно
# with open("test_write.txt", mode="wb") as file:
#     file.write(b"\nAnother random text")

# mode="ab" - добавляет бинарно
# b"\n..."
# with open("test_write.txt", mode="ab") as file:
#     file.write(b"\nAnother random text")

# # mode="ab" - читает
# # - бинарно
# with open("test_write.txt", mode="rb") as file:
#     for row in file:
#         print(row)


# class Student:

#     def __init__(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = list(grades) #[]
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
    
#     # def get_average(self):
#     #     return sum(self.grades) / len(self.grades)

# johnDoe = Student('John', 'Doe')
# # johnDoe = Student('John', 'Doe', [])
# janeDoe = Student('Jane', 'Doe')
# jamesSmith = Student('James', 'Smith')
# jennaSmith = Student('Jenna', 'Smith')
# print(johnDoe.grades is janeDoe.grades, jamesSmith.grades, jennaSmith.grades)

# students = johnDoe, janeDoe, jamesSmith, jennaSmith


with open("yolka.txt", mode="w+") as file:
    
    def p(n,a):
        if n==0:
            return
        else:
            print(a,end='')
            p(n-1,a)
        
            
    def foo(s,a):
        if s==0:
            return
        else:
            p(s,' ')
            p(a, '*')
            print()
            foo(s-1,a+2)
         
    foo(6,1)

file.close()