#Task 1
# list_1 = ['name', 'age', '1', '19']
#
# def hello_reversed():
#     a = list_1[0:len(list_1)//2]
#     b = list_1[len(list_1)//2:len(list_1)]
#     list_3 = a[::-1] + b[::-1]
#     print(list_3)
#
# hello_reversed()
import random


# Task 2
# def fibbo_number():
#     a = 1
#     b = 1
#     c = 0
#     numbers = [a,b]
#     for i in range(10):
#         c = a + b
#         a = b
#         b = c
#         numbers.append(c)
#     print(numbers)
#
# fibbo_number()

#Task 3
# number = 20
# number1 = 50
# def multy():
#     function = number + number1
#     print(function)
#
# def substr():
#     function = number - number1
#     print(function)
#
# def doublething():
#     multy()
#     substr()
#
# doublething()

#Task 4
# ask = input("Write file name - ")
#
# def file_name():
#     try:
#         with open(ask, "w") as my_file:
#             return my_file
#     except:
#         print(f"File name cannot be named like that ({ask}).")
#
# a = file_name()
#
# print(a)

#Task 5

# def gen_number():
#     import random
#     list1 = [0,4,4,4]
#     for i in range(6):
#         list2 = [1,4,5,7,9,0]
#         list1.append(random.choice(list2))
#     return list1
# a = gen_number()
# print(*a,sep="")









