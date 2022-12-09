import csv
import re


class Steam:
    purchases = {}
    games = []

    def __init__(self, enter_option):
        if enter_option == "registration": # registration
            self.register()
        elif enter_option == "login":
            self.login()
        else:
            print("Wrong option")

    # def purchase(self):
    #     """Купить игры, которые храняться в системе"""
    #     pass

    def register(self):

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        card = input("Enter your card: ")

        if name:
            self.name = name
            pattern = r"([a-zA-Z]+[^0-9])"
            result = re.fullmatch(pattern, name)
            if result:
                print("Correct name!")
            else:
                print("Name error")

        if email:
            self.email = email
            pattern = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
            result = re.fullmatch(pattern, email)
            if result:
                print("Correct email!")
            else:
                print("Email error")
                
        if password:
            self.password = password
            pattern = r"^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$"
            result = re.fullmatch(pattern, password)
            if result:
                print("Correct password!")
            else:
                print("password error")

        if card:
            self.card = card
            pattern = r"[0-9]{16}"
            result = re.fullmatch(pattern, card)
            if result:
                print("Correct card!")
            else:
                print("card error")

        if self.name and self.email and self.password and self.card:
            with open('users.csv', 'a', newline='') as file:
                headers = ['name', 'email', 'password', 'card', 'purchases', 'games']
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerow({headers[0]: name, headers[1]: email, headers[2]: password, headers[3]: card, headers[4]: None,headers[5]: None})
            
            

    def add_game(self):
        """Добавить игру в список игр(games)"""
        
        pass

    def login(self):
        """Вход в свой аккаунт, если он уже создан(проверить есть ли в списке игр)"""
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email and password:
            self.email = email
            self.password = password
            

        # Если email и Password есть в системе(файле)
        with open("users.csv", "r") as file:
            content = csv.DictReader(file)
            for row in content:
                print(row)
                if email in row ["email"]:
                    purchase_id = row["purchases"]


print("Choose a login method: registration, login")
enter_option = input("Write your choice: ")

person_1 = Steam(enter_option=enter_option)



