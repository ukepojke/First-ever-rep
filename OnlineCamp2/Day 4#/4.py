class Student:
    def __init__(self,name,group):
        self.name = name
        self.group = group

    def show(self):
        print(f"Name of the student is {self.name} and his group is {self.group}.")

    def __del__(self):
        print("This variable was deleted.")

stud1 = Student("Kaichi","4vk").show()

del stud1   

