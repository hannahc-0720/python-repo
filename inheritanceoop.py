# Superclass

class Pet():
    # Class constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

# Subclass

class Cat(Pet):
    def __init__(self, name):
        self.name = name
        
    def meow(self):
        print('Meow!')