class Human:
    def __init__(self, name , othername):
        self.name = "oleg"
        self.othername = "margo gosling"
        self.money = 100
        self.pleasure = 50
        self.health = 100


    def relax(self, hours):
        self.pleasure += hours * 10

        print(f"{self.name} на чиле на раслабоне.")

    def work(self, hours):
        income = hours * 20
        self.money += income
        print(f"{self.name} на заводе {hours} часов зато {income} мани на кармане.")

    def shopping(self, items_cost):
        if self.money >= items_cost:
            self.money -= items_cost
            self.pleasure += 30
            print(f"{self.name}пашол и купил ядерку.")
        else:
            print(f"{self.name} бедній бомжара.")

    def house(self):
        print(f"{self.name}дома не работая.")

    def relationship(self, other):
        self.pleasure += 30
        print(f"{self.name} занимається личнай жизню с {other.name}.")

    def life(self):
        self.health -= 5
        self.pleasure -= 5
        print(f"{self.name} вииживает.")
        self.money -= 20
        self.food +- 10


    def is_alive(self):
        return self.health > 0

    def info(self):
        print(f"Name: {self.name}, Money: {self.money}, Pleasure: {self.pleasure}, Health: {self.health}")

class Car:
    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def passengers_info(self):
        if self.passengers:
            print(f"в машині  {self.marka}, пасажирів: {', '.join(p.name for p in self.passengers)}")
        else:
            print("немає пасажирів.")

class Home:
    def __init__(self):
        self.food = 0
        self.cleanliness_level = 100

    def eat(self, human):
        if self.food > 0:
            self.food -= 1
            human.health += 10
            print(f"{human.name} наелса і спит.")
        else:
            print(f"нету шо кушать ((( {human.name}.")

    def clean(self):
        self.cleanliness_level = 100
        print("типерь чиста и красива.")

