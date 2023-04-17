#Task 1
# def add(num1,num2):
#     return num1 + num2
# a = add(5,7)
# print(a)
#
# def substract(num,num2):
#     a = num - num2
#     return a
# print(substract(3,5))
#
# def multiply(num1,num2):
#     return num1 * num2
# print(multiply(5,5))
#
# def divide(num1,num2):
#     return num1 / num2
# print(divide(5,2))

#Task 2
# def message_number(letter_length):
#     number = 0
#     for i in letter_length:
#         number += 1
#     print(f"You wrote {number} letters.")
#
# hello = input("write something - ")
#
# message_number(hello)

#Task 3
# dict1 = {"name": "ernest"}
# dict2 = {"age": 228}
#
# def dict_sum(a,b):
#     a.update(b)
#     return a
#
# dict_sum(dict1,dict2)
# print(dict1)

#Task 4
# def text_add():
#     with open("W:\desktop\menu.txt", "a") as my_file:
#         a = []
#         for i in range(1):
#             b = input("Write what you want to eat - ")
#             c = input("Write what you want to drink. - ")
#             a.append(f"To eat - {b}. To drink - {c}")
#             a = str(a)
#             my_file.write(a)
#
# text_add()

#Task 5
# def file_txt(hallo):
#     with open(hallo, "w") as my_file:
#         return my_file
#
# file_txt("das")

#Task 6
# def main_func():
#     print("Main function.")
#     def second_func():
#         print("I'm second function.")
#     second_func()
#
#
# main_func()

#Task 7
# hallo = {
#     "name": "ernest",
#     "age": 321,
#     "games": "dota"
# }
#
# def tuple_dic():
#     for i in hallo:
#         a = hallo.keys()
#         b = hallo.values()
#         a = tuple(a)
#         b = tuple(b)
#         return a,b
#
# print(tuple_dic())

#Task 8
# a = int(input("You're number - "))
# for i in range(2,a):
#     if a % i == 0:
#         print("Not prime number.")
#         break
# else:
#     print("Prime number.")
#Task 9
# def two_arg(func1,func2):
#     return a = [func1,func2]
#
#
# print(type(two_arg("hello world",2)))

#Task 10
# def numbers(hi):
#     a = []
#     for i in range(hi):
#         a.append(hi)
#     print(*a)
#     return a
#
# numbers(10)

#Task 11

# def user_sal():
#     import random
#     a = input("What's you're name? - ")
#     while True:
#         try:
#             b = int(input("What's you're salary? - "))
#             print(f"Name of this user - {a}\nSalary of this user - {b}")
#             break
#         except:
#             print(f"Name of this user - {a}\nSalary of this user - {random.randrange(5000,10000)}")
#             break
#
# user_sal()

#Task 12
# def element():
#     a = input("Write you're number - ")
#     list_lol = []
#     list_lol.append(str(a))
#     list_lol.append(int(a))
#     list_lol.append(float(a))
#     list_lol.append(bool(a))
#     list_lol.append(set(a))
#     list_lol.append(list(a))
#     list_lol.append(tuple(a))
#     print(list_lol)
#
# element()
