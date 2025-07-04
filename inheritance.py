# Superclass

class Pet():
    # Class constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def feed(self, food):
        print(f"{self.name} eats {food}.")

# Subclass

class Cat(Pet):
    # Inheriting the parent constructor
    def __init__(self, name, age, color):
        # super() refers to the class that is the superclass
        # using the superclass constructor to set up the subclass constructor
        super().__init__(name, age, color)
    
    # Specific to the child (sub) class
    def meow(self):
        print(f"{self.name} says: Meow!")

class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    
    def bark(self):
        print(f"{self.name} says: Ruff!")

cat1 = Cat("Troy", 7, "orange")
cat1.meow()
cat1.feed("fish")

dog1 = Dog("Leo", 1, "Dachshund")
dog1.bark()
dog1.feed("dog treats")