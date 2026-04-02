class Bank():
    def __init__(self):
        print("Let's open a bank account for you!")
    def create_acc(self):
        print("First we need to set up your details.")
        self.name=str(input("What is the name for this account? "))
        self.number=int(input("What is the number for this account? "))
        self.balance= int(input("What is your starting balance?"))
    def deposit(self):
        self.balance+= int(input("How much do you want to deposit?"))
        print("You have this much in your account: "+ str(self.balance))
    def widthdraw(self):
        self.balance-= int(input("How much do you want to widthdraw?"))
        print("You have this much in your account: "+ str(self.balance))
        print("The following are your details:")
        print(self.name)
        print(self.number)
        print("$"+str(self.balance))
object=Bank()  
object.create_acc()
object.deposit()
object.widthdraw()