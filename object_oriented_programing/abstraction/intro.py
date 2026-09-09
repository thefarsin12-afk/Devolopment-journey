#abstraction is hiding to class and methods
#using to all methods and atribute inheritance using class
#from abc import ABC,abstractmethod (using method),class ==>(ABC),method ==>@abstractmethod
"""
class Editor
   def start(self)
   def debug(self)
   def executing(self)

class Vscode(Editor)
   def start(self)   
   def dubug(self)   
   def executing(self)   
"""

from abc import ABC,abstractmethod
class Car (ABC):

    @abstractmethod
    def start(self):pass

    @abstractmethod
    def acceselotor(self):pass

    @abstractmethod
    def off(self):pass

class Baleno(Car):

    def start(self):
        print("Car start method")    

    def acceselotor(self):
        pass

    def off(self):
        pass   

baleno_instant = Baleno()
baleno_instant.start()

