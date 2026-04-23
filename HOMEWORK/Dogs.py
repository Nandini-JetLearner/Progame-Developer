class Dog:
    Names=["Cookie","Fluffy","Snowball"]
    Barks=["Woof Woof!","Ruufff! *pants","Awhoooo!"]

    def __init__(self,breed,color,size,activeness):
    
        self.breed=breed
        self.color=color
        self.size=size
        self.activeness=activeness
        print("Hello! This dog is up for adoption! :")

    def display(self):
        print(f"Breed: {self.breed}, Color: {self.color}, Size: {self.size}, Activeness: {self.activeness}")
        print("----------------------------------------")    

    def bark(self,y):
        print("This dog barks like this: " + (self.Barks[y]))

    def show_name(self,x):
        print("This dog's name is " + (self.Names[x]))

dog1= Dog("Labrador","yellow","Medium","moderate")
dog1.show_name(0)
dog1.bark(0)
dog1.display()

dog2= Dog("Huskie","grey & white","Large","Exercise frequently required")
dog2.show_name(1)
dog2.bark(1)
dog2.display()

dog3= Dog("Pomeranian","Cream/white","Small","Low")
dog3.show_name(2)
dog3.bark(2)
dog3.display()