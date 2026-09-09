"""
object orented programing = object oriented programming (real world representing) class,object

class = plan,design pattern,template,bluprint forn creating object

object = real world entity

self = using to current point instance

super() refrence tp parents class

__init__ = constractor 
using to initialization atributes

inheritance using to child class using tp parent class

constructer = intilaze atributes ,using to = __init__,no use to set(),
* constructer automatically creating object or a class

inheritance = child class access to parent class usning ()
type of inheritance(single,multi level,mulipile)

"""

class Animal:

    name:str
    sound:str

    def walk(self):

        print("animal is walking")

    def sleep(self):

        print("anumal is sleeping")

cat_instace = Animal()            

dog_instance = Animal()

elephent_instance = Animal()

elephent_instance.walk()