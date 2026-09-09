class Shape:

    name : str

    def __init__ (self,name):

        self.name = name

class Paarellelogram (Shape):

    base = int

    height = int

    def __init__ (self,name,base,height):

        super().__init__(name)

        self.base = base

        self.height = height

    def area(self):

      print("area of ",self.name,"=",self.base * self.height) 

palrelogram_instant1 = Paarellelogram("Parallogram ",12,45)
palrelogram_instant1.area()           