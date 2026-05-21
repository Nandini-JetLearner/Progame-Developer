#Multiple Inheritance
import random
Passwords=("A@sjgnl","jk0gjw","Wh0rkU32")
class Processor:
    def __init__ (self,):
        self.y=random.choice(Passwords)
    def process(self):
        print("Remeber this password. Password is: "+ (self.y))
        print("Processing information...")

class Storage:
    def store_data(self):
        print("Storing data...")

class Laptop(Processor, Storage):
    def Login(self,):
        self.x=input(str("Type in the password: "))
        if self.x == self.y:
            print("Correct!")
            print("_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_\n")
        else:
            print("Try again later.")

obj=Laptop()
obj.process()
obj.store_data()
obj.Login()

obj2=Laptop()
obj2.process()
obj2.store_data()
obj2.Login()