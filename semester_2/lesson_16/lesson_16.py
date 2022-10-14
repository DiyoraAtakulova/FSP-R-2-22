"""
Наследование
"""
class Parent:
    pass

class Child(Parent):
    pass


#  Пример
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Stock("murad building", 40, 2000).cost()

class Stock_2:
    n = 100
    def __init__(self, random):
        self.random = random
    
    def go(self):
        print(self.random)

class MyStock(Stock, Stock_2):
    def __init__(self, name, shares, price, funds):
        super().__init__(name, shares, price)
        # функция SUPER использует значения из отцовского класса

        # self.name = name
        # self.shares = shares
        # self.price = price
        self.funds = funds
        self.random = 12

    def cost(self):
        return self.funds * super().cost()

    # def sell(self, nshares):
    #     self.shares += nshares

# stock = Stock("murad building", 40, 2000)
my_stock = MyStock("golden house", 50, 1000, 12, 10000)
print(my_stock.cost())
my_stock.sell(10)
my_stock.go()
print(my_stock.shares, my_stock.n, my_stock.random)


""" HW: MRO | C1 LINEAR ALGORITHM """


# class Car:
#     model = "BMW"

#     def __init__(self, engine):
#         self.engine = engine

#     # def __str__(self):
#     #     return "{self.engine} {self.model}"

#     def get_car_model(self):
#         print(self.engine * 2)

#     def dummy_func(self):
#         print(2 + 5, self.engine)


# # print(Car.engine) # Car.engine не будет отображаться
# # Car("V8").get_car_model()
# # Car("V8").dummy_func()

# car_1 = Car("V12")
# car_1.get_car_model()
# # print(Car.model)


# from collections import namedtuple

# Point = namedtuple("Point", ["name", "y"])
# print(Point.__doc__)
# Point.x = 12
# print(Point.x)

