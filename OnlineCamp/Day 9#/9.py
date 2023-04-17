#Task 0
# while True:
#     try:
#         print("In this game, you will solve math. equations!")
#         max_number = int(input("Choose you're max. output number. - "))
#         if True:
#             break
#     except:
#         print("Choose only numbers!")
#
# import random
#
# b = 0
# c = 0
# while True:
#     try:
#         number1 = random.randint(0, max_number)
#         number2 = random.randint(0, max_number)
#         print(number1, "*", number2)
#         a = input("What's the right answer? - ")
#         if a == "exit":
#             print("Game over, you're score is! /////", "Right answers -", b, "Wrong answers - ", c)
#             break
#         elif int(a) == number1 * number2:
#             b += 1
#             print("You're right! New math problem for you. Be ready! ")
#         elif int(a) != number1 * number2:
#             print("You're not right, try again.")
#             c += 1
#
#     except:
#         print("Write only numbers!")



#Task 1
# import my_module
# my_module

#Task 2
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# list_lol = []
# for i in range(4):
#     list_lol.append(random.choice(names))
#
# print(list_lol)

#Task 3
# import sys
# print(sys.platform)

#Task 4

#Task 5
# from os import mkdir
# import random
# mkdir("W:\Desktop\lol")
# for i in range(5):
#     with open(f"W:\Desktop\lol\{random.randint(5,100)}.txt", "w") as f:
#         f.write("lol")

#Task 6
# import random
# names = ["AIBEK", "JOOMART", "ADINAI", "ERMEK", "ATAI", "ASLAN", "LYAZAT", "SALAVAT", "DANIYAR", "BOLOTBEK", "ALYMBEK", "DASTAN", "MAKSAT"]
# random.shuffle(names)
# com1 = names[0:4]
# com2 = names[4:7]
# com3 = names[7:10]
# com4 = names[10:13]
#
# print(com1)
# print(com2)
# print(com3)
# print(com4)

#Task 7

#Task 8
# import sys
# a = input()
# b = input()
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

#Task 9
# import random
# a = int(input("Write you're number - "))
# b = "qwertyuiopasdfghjklzxcvbnm123456789"
# password = []
# for i in range(a):
#     password.append(random.choice(b))
#
# a = "".join(password)
# print(a)

#Task 10
# import random
#
# print("Игра камень-ножницы-бумага! Напишите любое из этих слов и постарайтесь победить компьютер!")
#
#
# while True:
#     game = ["ножницы", "бумага", "камень"]
#     b = random.choice(game)
#     a = input("\nПишем сюда ваш выбор - ").lower()
#     if a == "ножницы" and b == "бумага":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы победили!")
#     elif a == "ножницы" and b == "камень":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы проиграли!")
#     elif a == "ножницы" and b == "ножницы":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Это ничья!")
#
#     elif a == "бумага" and b == "камень":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы победили!")
#     elif a == "бумага" and b == "ножницы":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы проиграли!")
#     elif a == "бумага" and b == "бумага":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Это ничья!")
#
#     elif a == "камень" and b == "ножницы":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы победили!")
#     elif a == "камень" and b == "бумага":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Вы проиграли!")
#     elif a == "камень" and b == "камень":
#         print(f"\nВы выбрали {a}\nКомпьютер выбрал {b}!\n")
#         print("Это ничья!")
#
#     elif a == "exit":
#         break

#Task 11
# import random
# print(random.randrange(6,12,2))
#
# for i in range(random.randrange(5,101),101):
#     if i % 5 == 0:
#         print(i)
#         break
#
# print(random.randrange(5,101,5))

#Task 12

# #Task 13
# from datetime import datetime, timedelta
# dt = datetime.now()
# td = timedelta(days=1000)
# my_date = dt + td
#
# print(my_date)


#Task 14
# NUMBERS = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# a = 0
# b = 0
# for i in range(len(NUMBERS) // 2):
#     sum = NUMBERS[a] + NUMBERS[a+1]
#     print(sum)
#     a += 2

#Task 15

# from datetime import datetime
#
# a = str(datetime.now())
# time = a[11:len(a)-7]
# print(time)

#Task 16
# import time
#
# for i in range(10):
#     time.sleep(i)
#     print("I love u <3")

#Task 17
# LIST1 = [1,3,5,7,9,11,13]
# LIST2 = [2,4,6,8,10,12,14]
#
# for i,j in zip(LIST1,LIST2):
#     print(i,j)




