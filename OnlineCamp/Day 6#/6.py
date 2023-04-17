#Task 1
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(6)
# print(dates_of_birth)

#Task 2
# a = {1}
# b = {2}
# c = {3}
# hello = set()
# hello.update(a,b,c)
# print(hello)

#Task 3
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#
# print(farm_2.difference(farm_1))

#Task 4

# hello_world = {"hello",1,3.14,True,"hiii"}
# hello_world.add(6)
# hello_world.pop()
# print(hello_world)

#Task 5
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu["Drinks"] = ["Coca-cola","Sprite","Fanta"]
# print(menu)

#Task 6
# method_set = {'.add("*")', '.remove("*")', '.clear()', '.update("*")', '.difference("*")', '.discard("*")', '.intersection("*")', '.intersection_update(*)', '.pop()'}
# method_dict = {'.clear()','.keys()','.items()','.get("*")','.values()','.update("*")'}
#
# print(method_set.intersection(method_dict))

#Task 7
# hello = {}
# for i in range(3):
#     a = input("You're name - ")
#     b = input("You're password - ")
#     hello[a] = b
# print(hello)

#Task 8

# data = {
#     "Ernest": "Programmer",
#     "Ignat": "Model",
#     "Rahim": "3dModeljer",
#     "Bakyt": "Musician",
#     "Tynchtyk": "DevOps"
# }
#
# for i in data:
#     print("Hello", i + ".", "Nice profession - " + data[i])

#Task 9
# numbers = set()
# hello = 0
# while hello < 10:
#     try:
#         for i in range(10):
#             hello_world = int(input("Type you're number - "))
#             numbers.add(hello_world)
#             hello += 1
#     except:
#         print("Type only numbers please.")
# not_hello_world = tuple(numbers)
# print(not_hello_world)

#Task 10
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu["besh_barmak"] = 130
# menu["besh_barmak"] = 135
# menu.pop("borsh")
# print(menu)

#Task 11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries = set(south_american_countries)
# south_american_countries = list(south_american_countries)
# print(south_american_countries)

#Task 12
# suitcase = []
# for i in range(5):
#     hi = input("Напишите что вы хотите взять с собой в чемодан - ")
#     suitcase.append(hi)
# suitcase.pop(4)
# print(suitcase)

#Task 13
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# i = farm_1.difference(farm_2)
# farm_3 = i
# farm_3.update(farm_2)
# print(i)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_1.difference(farm_2)
# print(farm_3)

