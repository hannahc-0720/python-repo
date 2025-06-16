
class Coordinate():
    # Create a class constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coords(self, x, y):
        print(f"The x value is {x}. The y value is {y}.")

c1 = Coordinate(4, 10)
c1.coords(4, 10)