import random
import datetime

def cr_car():
    a = input("Write you're car name! >>> ")
    return a

def parking_info():
    while True:
        try:
            b = int(input("\nHi again! How can I help you?\n\nWrite (1) to add you're car to the parking lot!\nWrite (2) to remove you're car from the parking lot!\nWrite (3) to see information about particular car!\nWrite (4) to see all cars that are now in the parking lot!\nWrite (5) to see all cars that left the parking lot!\nWrite (6) to create a personal car!\nWrite (0) to exit the parking lot.\n>>>>>>>>>>>>>>>> "))
            return b
        except:
            print("Write only numbers from 1 to 6!\n")


class Car:
    def __init__(self,car_name):
        self.car_name = car_name
        self.car_talon_str = ["A","B","C","D","F","a",'b','c','d','f']
        self.car_talon_int = random.randint(100,999)
        self.car_talon_int = str(self.car_talon_int)
        self.car_talon_final = []


    def comp_car(self):
        for i in self.car_talon_int:
            self.car_talon_final.append(i)
        self.car_talon_final.append(random.choice(self.car_talon_str))
        random.shuffle(self.car_talon_final)
        final = "".join(self.car_talon_final)
        print(f"You're car name is - {self.car_name}. You're token is - {final}")
        return [final, self.car_name]


class Parking:
    def __init__(self,max_parking_slots=5):
        self.max_parking_slots = max_parking_slots
        self.car_in = None
        self.car_out = None
        self.all_cars = []
        self.parking_only_car = []
        self.old_parking_cars = []

    def add_users_car(self,user_car: Car):
            self.all_cars.append(user_car)

    def add_parking_car(self):
        if len(self.parking_only_car) < self.max_parking_slots:
            user_inp = input("Write you're token >>> ")
            attempt = 0
            for i in self.all_cars:
                if user_inp in i[0]:
                    self.car_in = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")
                    self.parking_only_car.append([i[0],i[1],self.car_in])
                    print("\nThe car was successfuly added!\n")
                    attempt += 1
                    break
            if attempt == 0:
                print("\nInvalid talon.")
        else:
            print("Not enough space in parking.")

    def remove_parking_car(self):
        user_int = input("Write you're token >>> ")
        attempt = 0
        for i in range(len(self.parking_only_car)):
            if user_int in self.parking_only_car[i]:
                rem_car = self.parking_only_car.pop(i)
                self.car_out = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")
                self.old_parking_cars.append([rem_car[0],rem_car[1],rem_car[2],self.car_out])
                print(f"The car with this talon - {user_int} - has been successfully removed from the parking lot!\n")
                attempt += 1
                break
        if attempt == 0:
            print(f"There are no car's with this - {user_int} - talon.")

    def show_particular_car(self):
        user_int = input("Write you're token >>> ")
        attempt = 0
        for i in self.parking_only_car:
            if user_int in i[0]:
                attempt += 1
                print(f"\nCar's brand is - {i[1]}\nThe time the car was parked in - {i[2]}\n")
        for i in self.old_parking_cars:
            if user_int in i[0]:
                attempt += 1
                print(f"\nCar's brand is - {i[1]}\nThe time the car was parked in - {i[2]}\nThe time the car left the parking lot - {i[3]}\n")
        if attempt == 0:
            print(f"\nThere are no car's with this - {user_int} - talon.")

    def show_all_cars_current(self):
        print(self.parking_only_car)

    def show_all_cars_old(self):
        print(self.old_parking_cars)






