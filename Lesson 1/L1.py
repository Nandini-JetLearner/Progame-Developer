import random
class student():
    Houses=["Ravenclaw","Gryffindor","Hufflepuff","Slytherin"]
    name=""
    age=0
    grade= ""
    house=random.choice(Houses)
    teacher="Ms. Godbole"

    def __init__(self):
        print("Let's add a new student!")

    def choose_details(self):
        self.name=str(input("What is the student's name?"))
        self.age=int(input("How old is the student?"))
        self.grade=int(input("What number grade is the student in?"))

    def show_details(self):
        print("The folowing are the details of our new student:")
        print (self.name)
        print (str(self.age) + " years old")
        print (str(self.grade) + "th grade")
        print (self.house)
        print (self.teacher)
        

object=student()
object.choose_details()
object.show_details()
objecta=student()
objecta.choose_details()
objecta.show_details()