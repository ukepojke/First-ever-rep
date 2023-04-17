#Task 1

#Task 2
# with open("user.txt", "w") as data:
#     i = input("you're login - ")
#     j = input("you're password - ")
#     data.write(i + " " + j)

#Task 3
# with open("people.txt", "w") as my_file:
#     i = input("Write something here - ")
#     my_file.write(i)
# with open("people.txt", "r") as my_file:
#     j = my_file.read()
#     if "w" in j:
#         print("There is 'w' in here.")
#     else:
#         print("There is no 'w' in here")

#Task 4
# with open("python.txt", "w") as data:
#     data.write('''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.''')
#
#
# with open("python.txt", "r") as data:
#     some_text = data.read()
#
# hello = some_text.split(" ")
# t_words = []
#
# for i in hello:
#     if "t" in i:
#         t_words.append(i)
# print(t_words)

#Task 5
# def database():
#     with open("database.txt", "a") as user_info:
#         user_info.write(f",{login} {password}")
#
# with open("database.txt", "r") as data:
#     data = data.read()
# data_user = data.split(",")
# true_data = 0
#
# while true_data == 0:
#     ask = input("You want to sign up or login in?\nPrint 'sign up' to sign up or 'login' to login in. - ").lower()
#     user_number_try = 3
#     pass1_try = 3
#     else_try = 1
#     if ask == "login":
#         login = input("Write you're login here - ")
#         password = input("Write you're password here - ")
#         for i in data_user:
#             if login == i.split(" ")[0] and password == i.split(" ")[1]:
#                 print("You were successfully logged in!\n")
#                 else_try -= 1
#                 true_data += 1
#                 break
#             elif login == i.split(" ")[0] and password != i.split(" ")[1]:
#                 while user_number_try > 0:
#                     pass1_try -= 1
#                     user_number_try -= 1
#                     print(f"Password is incorrect, try again. ({pass1_try} tries left)")
#                     password = input("Write you're password here - ")
#                     if password == i.split(" ")[1]:
#                         print("You were successfully logged in!\n")
#                         else_try -= 1
#                         true_data += 1
#                         break
#                     elif pass1_try == 0:
#                         print("Sorry, password is incorrect.")
#                         else_try -= 1
#                         break
#         if else_try == 1:
#             print(f"This login does not exist. We can register you by this nickname - {login}.")
#             while True:
#                 password = input("Write you're password here - ")
#                 password1 = input("Write you're password again - ")
#                 if password == password1:
#                     print("We successfully signed you up!\n")
#                     true_data += 1
#                     database()
#                     break
#                 else:
#                     user_number_try -= 1
#                     pass1_try -= 1
#                     print(f"You're passwords does not match up. Please write the same password two times. ({pass1_try} tries have left)\n")
#                     if user_number_try == 0:
#                         print("You couldn't write the same password twice.\n")
#                         break
#     elif ask == "sign up" or ask == "signup":
#         login = input("Write you're login here - ")
#         while True:
#             password = input("Write you're password here - ")
#             password1 = input("Write you're password again - ")
#             if password == password1:
#                 print("We successfully signed you up!\n")
#                 true_data += 1
#                 database()
#                 break
#             else:
#                 user_number_try -= 1
#                 pass1_try -= 1
#                 print(f"You're passwords does not match up. Please write the same password two times. ({pass1_try} tries have left)\n")
#                 if user_number_try == 0:
#                     print("You couldn't write the same password twice.\n")
#                     break

#Task 6

# a = input("Write you're login here - ")
# b = input("Write you're password here - ")
#
# while True:
#     c = input("Upload you're photo here - ")
#     try:
#         with open(c, "rb") as my_file:
#             my_file.read()
#             print("You were successfully logged in!")
#             with open("user_profile.txt", "a") as f:
#                 f.write(f"\nUser name - {a}\nUser password - {b}\nUser photo - {c}\n")
#                 break
#     except:
#         print("Invalid photo link.\n")

# W:\Desktop\GriffithBerserk.png

#Task 7

# while True:
#     count = 0
#     count1 = 0
#     a = input("What file you want to change? -")
#     b = input("To what file you want to change first file? - ")
#     try:
#         with open(a, "rb") as my_file:
#                 my_file.read()
#     except:
#         count += 1
#     try:
#         with open(b, "rb") as my_file:
#                 my_file.read()
#     except:
#         count1 += 1
#
#     if count == 1 and count1 == 1:
#         print("Both files doesn't exist.")
#     elif count1 == 1:
#         print("Second file doesn't exist.")
#     elif count == 1:
#         print("First file doesn't exist.")
#     else:
#         a = b
#         try:
#             with open(a, "rb") as my_file:
#                 my_file.read()
#                 print("Successfully changed files.")
#                 print(str(a))
#                 break
#         except:
#             print("Error, file doesn't exist.")

# W:\Desktop\GriffithBerserk.png / W:\Desktop\3bc.jpg

#Task 8
# with open("months.txt", "w") as f:
#     f.write('''
#     January       18000
#     February      32641
#     March         28300
#     April         11200
#     May           21100
#     June          19000
#     July          8000
#     August        72000
#     September     12300
#     October       17000
#     November      25000
#     December      30000
#     ''')

# with open("months.txt", "r") as f:
#     numbers = f.read()
#
# numbers = numbers.replace(" ", "")
# numbers = numbers.split("\n")
# numbers = list(numbers)
# numbers = numbers[1:len(numbers)-1]
# def months_delete(func):
#     lol = []
#     for i in func:
#         if "May" in i:
#             lol.append(i)
#         elif "July" in i:
#             lol.append(i)
#         elif "September" in i:
#             lol.append(i)
#         elif "November" in i:
#             lol.append(i)
#     return lol
#
# new_number = months_delete(numbers)
# just_numbers = []
# for i in new_number:
#     just_numbers.append(int("".join(j for j in i if j.isdigit())))
#
# def number_conclusion(func):
#     nummm = 0
#     for i in func:
#         nummm += i
#     nummm = nummm / 4
#     return nummm
#
# just_numbers = number_conclusion(just_numbers)
# print(f"Среднее арифметическое этих 4 месяцев составляет - {just_numbers}")

#Task 9
# with open("integer_number.txt", "w") as f:
#     f.write("10,24,3401,351111,229,1920,1000")


# with open("integer_number.txt", "r") as f:
#     numbers = f.read()
#
# numbers = numbers.split(",")
# numbers_list = []
# for i in numbers:
#     numbers_list.append(int(i))
#
# final_number = [min(numbers_list),max(numbers_list)]
#
# with open("integer_number_max_min.txt", "w") as f:
#     f.write(f"{final_number}")

#Task 10
#
# user_input = input("Write you're text here. - ")
#
# user_input = user_input.split(" ")
# user_input = list(user_input)
# new_list = []
# for i in user_input:
#     new_list.append(i+"\n")
#
# with open("user_input.txt", "w") as f:
#     for i in new_list:
#         f.write(i)





















