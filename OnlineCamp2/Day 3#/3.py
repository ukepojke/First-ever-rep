# #Task 1
# class Factory:
#     def engine(self):
#         a = "Двигатель создан"
#         return a
#
#     def bridge(self):
#         a = "Ходовая часть создана"
#         return a
#
#
# class Toyota(Factory):
#     def wheels(self):
#         a = "Колеса готовы"
#         return a
#
#     def windows(self):
#         a = "Стекла готовы"
#         return a
#
# car = Toyota()
#
# m1 = car.engine()
# m2 = car.bridge()
# m3 = car.wheels()
# m4 = car.windows()
# m_list = [m1,m2,m3,m4]
#
# print(m_list)

#Task 2

# class Zoo:
#     def __init__(self, animal_1, animal_2, animal_3):
#         self.animal_1 = animal_1
#         self.animal_2 = animal_2
#         self.animal_3 = animal_3
#         self.animal_4 = []
#
#     def print_zoo(self):
#         return (self.animal_1,self.animal_2,self.animal_3,self.animal_4)
#
#     def change_name(self,change_name_1):
#         self.animal_1 = change_name_1
#         self.animal_4.append(change_name_1)
#
#     def change_name1(self,change_name_3):
#         self.animal_3 = change_name_3
#         self.animal_4.append(change_name_3)
#
#
# zoo = Zoo("Tiger","Behemoth","Jiraf")
# zoo.change_name("Leon")
# zoo.change_name1("Snake")
# print(zoo.print_zoo())


