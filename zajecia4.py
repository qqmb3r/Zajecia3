class Rectangle:
    def __init__(self,a,b):
        self.a = 8
        self.b = 9
    def set_params(self,a,b):
        self.a = a
        self.b = b
    def calc_surface(self):
        return self.a*self.b
    def __repr__(self):
        return "Rectangle["+str(self.a) + " by " + str(self.b) + "]"
r1 = Rectangle(8,9)
print(r1.calc_surface())

