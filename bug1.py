class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        

class Circle(Base): #added the Base class as a parent class
    def __init__(self, x, y, size): #added the y paramerter
        super().__init__(x, y, size) #pass the values to the parent constructor
        
    def shape(self): #returns the shape type
        return "This is a circle"
    def draw(self):
        return f"""
    ({self.x}, {self.y})\n{self.size}
    , - ~ ~ ~ - ,
, ' ' ,
, ,
, ,
, ,
, ,
, ,
, ,
, ,
, , '
' - , _ _ _ , '

    """
#I tried to copy the circle text from the homework pdf and from the pdf provided in the announcement but both wont copy the spacing correctly.

def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())


main()