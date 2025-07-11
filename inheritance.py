'''
Inheritance with Classes & Objects
'''

# Superclass
class Pet():
    # Class constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    # Since the function is in the superclass, it can be used in any subclass
    def feed(self, food):
        print(f"{self.name} eats {food}.")

# Subclass
class Cat(Pet):
    # Inheriting the parent constructor
    def __init__(self, name, age, color):

        super().__init__(name, age, color) # super() refers to the the superclass
    
    # Specific to the subclass, meaning any other subclass can't run this function
    def meow(self):
        print(f"{self.name} says: Meow!")

class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    
    # Specific to the subclass
    def bark(self):
        print(f"{self.name} says: Ruff!")

cat1 = Cat("Troy", 7, "orange")
cat1.meow() # The function only specific to this subclass
cat1.feed("fish") # The function from the superclass available to all subclasses

dog1 = Dog("Leo", 1, "Dachshund")
dog1.bark()
dog1.feed("dog treats")