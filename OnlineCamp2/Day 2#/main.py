from imp import Car, Parking, cr_car, parking_info




first_parking = Parking()

is_this_true = True

while is_this_true:
    a = input("Hi. Shall we create a personal car for you?\n\nWrite (yes) to create a car or (no) to go further. >>> ")
    if a.lower() == "yes":
        user_car = cr_car()
        user_car = Car(user_car)
        user_car = user_car.comp_car()
        first_parking.add_users_car(user_car)
        while True:
            parking_answer = parking_info()
            if parking_answer >= 0 and parking_answer < 7:
                if parking_answer == 1:
                    first_parking.add_parking_car()
                elif parking_answer == 2:
                    first_parking.remove_parking_car()
                elif parking_answer == 3:
                    first_parking.show_particular_car()
                elif parking_answer == 4:
                    first_parking.show_all_cars_current()
                elif parking_answer == 5:
                    first_parking.show_all_cars_old()
                elif parking_answer == 6:
                    break
                elif parking_answer == 0:
                    is_this_true = False
                    break
                else:
                    print("Write only number from 1 to 6.\n")

    elif a.lower() == "no":
        while True:
            try:
                parking_answer = parking_info()
                if parking_answer > 0 and parking_answer <= 6:
                    if parking_answer == 1:
                        first_parking.add_parking_car()
                        break
                    elif parking_answer == 5:
                        break
                    elif parking_answer == 6:
                        is_this_true = False
                        break
                else:
                    print("Write only number from 1 to 6.\n")
            except:
                print("Write only numbers to be able to access the parking features.\n")

    elif a.lower() != "yes" or a.lower() != "no":
        print("I don't understand. Write only (yes/no).\n")

print("Goodbye!")

