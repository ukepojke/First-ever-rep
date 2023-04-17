# final_grade = int(input("Write you're final score: "))
# if final_grade >= 90:
#     print("Gratz, you're [A] rank")
# else:
#     if final_grade >= 70:
#         print("Gratz, you're [B] rank")
#     else:
#         if final_grade >= 50:
#             print("Gratz, you're [C] rank")
#         else:
#             if final_grade < 50:
#                 print("You didn't pass exam")

# a = int(input())
# for i in a:
#     a = a + 1
#     print (i)
#
# word = "LightCode"
# for i in range(len(word)):
#     print(i+1, word[i])



# data = {
#     "Ernest": "Programmer",
#     "Ignat": "Model",
#     "Rahim": "3dModeljer",
#     "Bakyt": "Musician",
#     "Tynchtyk": "DevOps"
# }

# base.txt", "w") as data:
#     data.write("ernest 12345,matvey 54321,ignat 228")
#
# with open("database.txt", "r") as data:
#     data = data.read()
# data_user = data.split(",")
# number_try = 0
# user_data = []
# while True:
#     a = input("You want to sign up or login in? - ").lower()
#     if a == "login":
#         print("To login in you need to write down you're login and password!")
#         for i in data_user:
#             b = input("Print you're login - ")
#             if b == i.split(" ")[0]:
#                 while number_try < 5:
#                     c = input("Print you're password - ")
#                     if b == i.split(" ")[0] and c == i.split(" ")[1]:
#                         print("You logged in!")
#                         break
#                     else:
#                         print("Password is incorrect.")
#                         number_try += 1
#                 else:
#                     print("You're t")
#             else:
#                 print(f"This login does not exist, let's register you.'{b}' is you're login now.")
#                 c = input("Print you're password - ")
#     elif a == "sign up" or a == "signup":
#         print("To sign up you need to write down you're login and password!")
#         b = input("Print you're login - ")
#         c = input("Print you're password - ")
#     else:
#         print("Sorry, I don't understand. Print sign up or login.")




# login = input('Print your login - ')
# password = input('Print your password - ')
# image = input('Print direction of your photo - ')
#
# with open('/Users/cer6erus7/Documents/GriffithBerserk.png', 'ab') as p:
#     if image == '/Users/cer6erus7/Documents/GriffithBerserk.png':
#
#         with open('database1.txt', 'w') as f:
#             f.write(f'{login}, {password}, {image}')
#     else:
#         print('Wrong direction of your photo!')

# import random as rd
# random_number = rd.randint(0, 10)
# count = 0
# user_number = 0
# while count < 3:
#     user_number = int(input('Write your number?   '))
#     if user_number == random_number:
#         print('You wrote correct number')
#         break
#     elif user_number != random_number:
#         count += 1
# else:
#     print('you lose')

# def whas_number():
#     import random
#     user_number = []
#     while True:
#         try:
#             a = int(input("What's the length of the max. number? - "))
#             if a < 7 or a > 30:
#                 print("Min or max length of the number must be at least 7,30.")
#             else:
#                 break
#         except:
#             print("Wrong value.\n")
#     for i in range(3):
#         try:
#             b = input("What numbers should be in generator?(write number and ',' or ' ') - ")
#             if " " in b and "," in b:
#                 print("Wrong value.\n")
#             elif " " in b:
#                 while True:
#                     b = b.split(" ")
#                     if len(b) < 3:
#                         print("Must be at least 3 numbers.\n")
#                     elif len(b) >= 3:
#                         while len(user_number) < a:
#                             user_number.append(random.choice(b))
#                         return int("".join(user_number))
#                     break
#             elif "," in b:
#                 while True:
#                     b = b.split(",")
#                     if len(b) < 3:
#                         print("Must be at least 3 numbers.\n")
#                     elif len(b) >= 3:
#                         while len(user_number) < a:
#                             user_number.append(random.choice(b))
#                         return int("".join(user_number))
#                     break
#         except:
#             print("Something went wrong...")
#
import random
print(random.randrange(0, 10))