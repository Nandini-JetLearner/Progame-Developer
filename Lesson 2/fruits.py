class Fruit:
    fruit_count=0
    def __init__(self,color,taste,shape,preference):
        self.color=color
        self.taste=taste
        self.shape=shape
        self.preference=preference

        Fruit.fruit_count+=1
        self.fruit_number=Fruit.fruit_count
    
    def get_shape(self):
        return self.shape
    
    def set_shape(self, new_shape):
        self.shape=new_shape

    def increase_preference(self):
        self.preference+=1
    
    def showFruit(self):
        print(f"This is Fruit{self.fruit_number}")
        print(f"Color: {self.color}, shape: {self.shape}, Preference: {self.preference}")
        print("----------------------------------------")    

apple= Fruit("red","sweet","round",1)
apple.increase_preference()
print("Shape of fruit",apple.fruit_number,":",apple.get_shape())
apple.set_shape("sphere")
apple.showFruit()

banana= Fruit("yellow","sweet","curved",2)
banana.increase_preference()
print("Shape of fruit",banana.fruit_number,":",banana.get_shape())
banana.set_shape("Irregular Cylinder")
banana.showFruit()

mango= Fruit("orange","sweet&sour","round",3)
mango.increase_preference()
print("Shape of fruit",mango.fruit_number,":",mango.get_shape())
mango.set_shape("Elongated Sphere")
mango.showFruit()