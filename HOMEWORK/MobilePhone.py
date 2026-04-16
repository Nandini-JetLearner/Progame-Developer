import random
class MobilePhone():

    def __init__(self):
        Times=["10:24","4:25","10:26","12:27","10:18","11:11","8:08"]
        self.time=random.choice(Times)
        self.year=2008
        self.model=14
        self.battery=100
        print("Welcome to your phone!")
    
    def use_phone(self):
        x=str(input("Do you want to use your phone?"))
        if x == "yes"or x== "Yes":
            self.battery-=5
            print("Using phone.")
            print("Your battery is now "+str(self.battery)+"%")

    def check_details(self):
        y=str(input("Do you want to check your phone's details?"))
        if y == "yes"or y == "Yes":
            print("Model: "+ str(self.model))
            print("Year Manufactured: "+ str(self.year))

    def check_time(self):
        z=str(input("Do you want to check the time?"))
        if z == "yes"or z == "Yes":
            print(self.time)
        print("Thank's for using Mobile Phone!")
        

object=MobilePhone()  
object.use_phone()
object.check_details()
object.check_time()