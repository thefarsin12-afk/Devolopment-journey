#object oriented method
class Book:

    title:str
    price:float
    pages:int
    auther:str

    def __init__(self,title,price,pages,auther):

        self.title = title

        self.price = price

        self.pages = pages

        self.auther = auther

    def get_book(self):

        print(self,self.title,self.price,self.pages,self.auther)

randamuzham_instance = Book("randamuzham",650,550,"mt")
randamuzham_instance.get_book()

sherlockhomes_instance = Book("Sherlockhomes",1020,610,"sherlock")
sherlockhomes_instance.get_book()