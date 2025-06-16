
# Step 1: Create a pet/animal class with the following 3 properties
    # name, age, color
# Step 2: Create two objects from that pet class with different data filled in
# Step 3: Print out each property of one of the objects like so:
    # Name: Betty
    # Color: brown
    # Age: 5

# BONUS: Using string formatting, display one object's data in this format:
    # Betty is a brown cow and is 5 years old.

class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

turtle = Animal("Lulu", 4, "green")
print(f"{turtle.name} is a {turtle.color} turtle and is {turtle.age} years old.")

cat = Animal("Sigge", 6, "orange")
print(f"{cat.name} is a {cat.color} cat and is {cat.age} years old.")


class Ice_Cream:
    def __init__(self, flavor, scoops, base):
        self.flavor = flavor
        self.scoops = scoops
        self.base = base

flavor = input("Enter the flavor: ")
scoops = int(input("Enter the number of scoops: "))
base = input("Enter the base (cone or cup): ")

ice_cream1 = Ice_Cream(flavor, scoops, base)
print(f"You ordered {ice_cream1.scoops} scoop(s) of {ice_cream1.flavor} ice cream in a {ice_cream1.base}.")