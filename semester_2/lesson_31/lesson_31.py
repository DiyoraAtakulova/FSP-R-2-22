# if "behruz" in "My name is behruz":
#     print(True)

# if 1 in [1,2,3]:
#     print(True)

import re

pattern = re.compile('for') # может содержать в себе уникальные символы
string = 'Look for the specific word for if you can. :1'
# print(string[5], string[7]) 
# str_2 = "hdgfdghg"
print('for' in string)
# print(re.search(pattern, string)) # уникальный РЕ объект
# print(re.search(pattern, str_2)) # None

# # Для чего нужен РЕ объект:
# result = re.search(pattern, string) # result - уникальный РЕ объект
# print("group", result.group()) # group() находит то что в result
# print(result.span()) # индекс от start до end
# print(result.start())
# print(result.end()) # 8 не включительно

# result = re.findall(pattern, string) # выводит в список все возникновения искомой строки
# print(result)

# pattern = re.compile('Look for the specific word for if you can. :1')
# result = re.fullmatch(pattern, string) # проверяет равны ли строки между собой
# # print(result) # если равны,то возвращает РЕ объект
# print(result.group()) # вернет строку


''' 
    r - означает что строка игнорирует любые символы типа \n \t и тд. 
    [a-zA-Z] - находит любой символ в диапазоне букв a-z и A-Z 
    . - находит любой символ 
    t - находит букву t 
    В итоге мы получаем программу, которая находит 3 символа: 
        Первое - любая буква анг алфавита 
        Второе - любой символ 
        Третье - букву t 
    Если он не неходит букву t, то мы не получаем ответ 
''' 
# string = '123Look for the specific tword for if you can. :1' 
# pattern = re.compile(r"([a-zA-Z]).([t])") 
# result = pattern.search(string) 
# print(result)


# r"yes, no \n \t" или re.compile()  -  УНИКАЛЬНЫЙ ПАТТЕРН РЕГУЛЯРНОГО ВЫРАЖЕНИЯ





import csv
class Steam:
    purchases = {}
    games = []

    def __init__(self, enter_option):
        if enter_option == "регистрация":
            self.register()
        elif enter_option == "логин":
            self.login()
        else:
            print("Неправильная опция")


    # def __init__(self, name, email, password, card):
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.card = card

    def purchase(self):
        """Купить игры, которые храняться в системе"""
        pass

    def register(self):
        """Регистрация пользователя, если его нет в системе
        
        Шаги для регистрации:
            1. Принять все данные
            2. Проверить правильность данных
                - имя должно хранить только буквы
                - правильность написания email
                - требования для пароля
                - проверить правильность ввода данных карт(16 чисел)
            3. Если проверка прошла - создать пользователя, то есть сохранить в файл
            4. Если не прошло, то ввести данные правильно

        """
        name = input()
        email = input()
        password = input()
        card = input()

        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        if card:
            self.card = card
        
        if self.name and self.email and self.password and self.card:
            # написать логику записи данных в файл
            pass

    def add_game(self):
        """Добавить игру в список игр(games)"""
        pass

    def login(self):
        """Вход в свой аккаунт, если он уже создан(проверить есть ли в списке игр)"""
        email = input()
        password = input()
        if email:
            self.email = email
        if password:
            self.password = password

        # Если email и Password есть в системе(файле)
        with open("users.csv", "r") as file:
            content = csv.DictReader(file)
            for row in content:
                print(row)

        pass

# print("Выберите способ входа: регистрация, логин")
# enter_option = input("Напишите свой выбор:")

# person_1 = Steam(enter_option=enter_option)
# # person = Steam("Diyora","diyora@gmail.com", "admin123", {}, 
# #                 [], {"code": '1233 4545 5656 7869', "money": 1000})


with open("users.csv", "r") as file:
    content = csv.DictReader(file)
    for row in content:
        print(row)
        if "behruz" in row["name"]:
            purchase_id = row["purchases"]

with open("purchases.csv") as file:
    content = csv.DictReader(file)
    for row in content:
        if row["user"] == purchase_id:
            print(row)


"""
# УЗНАТЬ КОЛИЧЕСТВО СТРОК В ФАЙЛЕ
file = open("purchases.csv")
num = len(file.readlines()[1:])
print(num)
"""