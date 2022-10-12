""" 
Создать класс, описывающий персонажа/игрока с переменными: 
username, email, password, health, abilities, specialization, items (можно создать еще)

У класса должно быть три метода:
    1. Войти в игру: если пароль и логин правильные, то вернуть в ответ сообщение об удачном логине,
        если не правильные - об обратном
    2. Дать пользователю возможность выбора специализации. 
        Специализации создайте сами. Пример: (рыцарь, гта персонаж, и что-то ещё)
    3. После выбора персонажа, у него должен создаться персонаж с начальными параметрами. Пример

health=100
specialization=assassin 
abilities=(список возможностей)
items=(список вещей которые у него есть)
"""

class Player:
    # STRENGTH = "сила"
    # AGILITY = "ловкость"
    # INTELLECT = "разум"
    """
    Для удобства создать отдельный файл для переменных/констант
    """
    available_specialization = {"сила":"Сила", "рузум":"Рузум", "ловкость":"Ловкость"} # input split
    available_abilities = {
        "сила":("Таран"), 
        "рузум":("Огненный шар"), 
        "ловкость":("Уклонение"),
    }
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.health = 100
        self.abilities = []
        self.specialization = ""
        self.items = []

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("You logged in succesfully!")
        else:
            print("Usename or password is invalid")
    
    def choose_specialization(self, specialization):
        if specialization in self.available_specialization.values():
            self.specialization = specialization
            self.create_hero()
            print(f"Вы выбрали {specialization}!")
        else:
            print("Вы ввели неправильную специализацию!")

    def create_hero(self):
        if self.specialization == self.available_specialization["сила"]:
            self.health = 200 
            self.abilities = self.available_specialization[self.specialization.lower()]
            self.items = ["меч"]
            print("Выбрал силу")
        elif self.specialization == self.available_specialization["ловкость"]:
            self.health = 200 
            self.abilities = self.available_specialization[self.specialization.lower()]
            self.items = ["лук"]
            print("Выбрал ловкость")
        elif self.specialization == self.available_specialization["разум"]:
            self.health = 200 
            self.abilities = self.available_specialization[self.specialization.lower()]
            self.items = ["посох"]
            print("Выбрал разум")
            


strength = Player("Aloha", "123admin")
username = "Aloha"
password = "123admin"
specialization = "Сила"

strength.login(username, password)
strength.choose_specialization(specialization)

