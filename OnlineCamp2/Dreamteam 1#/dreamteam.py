
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.


# class Guns:
#     def __init__(self,gun_name,gun_capacity=10):
#         self.gun_name = gun_name
#         self.gun_capacity = gun_capacity
#
# class Soldier(Guns):
#     def __init__(self,soldier_name,gun_name,gun_capacity):
#         super().__init__(gun_name,gun_capacity)
#         self.soldier_name = soldier_name
#
# class ActOfShooting(Soldier):
#     def __init__(self,soldier_name,gun_name,gun_capacity):
#         super().__init__(soldier_name,gun_name,gun_capacity)
#         self.current_bullets = gun_capacity
#
#     def shoot(self):
#         if self.gun_capacity != 0:
#             self.gun_capacity -= 1
#             print(f"Pew-pew! 1 bullet has been shot. {self.gun_capacity} bullets have left.")
#         if self.gun_capacity == 0:
#             print(f"No ammo left. Try to reload.")
#
#     def reload(self):
#         self.gun_capacity = self.current_bullets
#         print(f"\nSuccessfully reloaded. You're mag is {self.current_bullets} bullets now! You good to go!\n")
#
#
# first_shoot = ActOfShooting(gun_name="ak47",gun_capacity=5,soldier_name="Ryan")
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.shoot()
# first_shoot.reload()
# first_shoot.shoot()
# first_shoot.shoot()


# # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.



# class Furniture:
#     def __init__(self, name, area: (int,float)):
#         self.name = name
#         self.area = area
#
#     def return_value(self):
#         return [self.name,self.area]
#
# bed = Furniture("bed",4).return_value()
# wardrobe = Furniture("wardrobe",2).return_value()
# table = Furniture("table",1.5).return_value()
#
# lst = [bed,wardrobe,table]
#
# class Home:
#     def __init__(self,home_type,overall_area: (int,float),furniture: list):
#         self.home_type = home_type
#         self.overall_area = overall_area
#         self.furniture = furniture
#         self.area_left = 0
#
#     def __repr__(self):
#         for i in self.furniture:
#             self.area_left += i[1]
#         return f"\nHouse type - {self.home_type}.\nOverall area of the {self.home_type} is {self.overall_area}.\nAvailable area in the {self.home_type} is {self.overall_area - self.area_left}.\n{self.home_type}'s furniture list are {self.furniture}."
#
#
#
# house_home = Home("Apartment",10,lst).__repr__()

# print(house_home)








# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

#
# class Student:
#     def __init__(self,name,age,major):
#         self.name = name
#         self.age = age
#         self.major = major
#
#     def __str__(self):
#         return f"name: {self.name}, age: {self.age}, major: {self.major}"
#
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
#
# print(Steve)
# print(Johnny)


# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()


# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3



# class MoneyFmt:
#     def __init__(self,money: float):
#         self.money = f"${money:-,.2f}"
#
#     def update(self,new_money):
#         self.money = f"${new_money:-,.2f}"
#
#     def __repr__(self):
#         if "-" in self.money:
#             return f"-0{self.money[len(self.money)-3:len(self.money)]}"
#         return f"0{self.money[len(self.money)-3:len(self.money)]}"
#
#     def __str__(self):
#         return self.money
#
#
# a = MoneyFmt(321312.5512321321312124512511)
# print(a)
# a.update(7467456.417519519129312312)
# print(a)
# print(a.__repr__())
# print(a.__str__())



# # 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle

# import random
#
#
# class Card:
#     def __init__(self):
#         self.tup = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
#
#
# class DeckOfCards:
#     def __init__(self,tuplik):
#         self.hearts = ["Heart" + "(" + i + ")" for i in tuplik.tup]
#         self.diamonds = ["Diamond" + "(" + i + ")" for i in tuplik.tup]
#         self.clubs = ["Club" + "(" + i + ")" for i in tuplik.tup]
#         self.spades = ["Spade" + "(" + i + ")" for i in tuplik.tup]
#
#         self.cards = self.hearts + self.diamonds + self.clubs + self.spades
#
#     def random_card(self):
#         if len(self.cards) > 0:
#             rand_c = random.choice(self.cards)
#             self.cards.remove(rand_c)
#             return rand_c
#         return "Нету карт в колоде."
#
#     def shuffle_shuffle(self):
#         if len(self.cards) == 52:
#             random.shuffle(self.cards)
#         else:
#             print("Нету карт.")
#
#     def __str__(self):
#         print(len(self.cards))
#         print(self.cards)
#
# card = Card()
# b = DeckOfCards(card)
# b.shuffle_shuffle()
# b.random_card()
# b.__str__()
# b.shuffle_shuffle()







        
