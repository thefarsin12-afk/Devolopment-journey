#multi level inheritance:-

class Grandparent:

    def propreties(self):
        print("2 acres")

class Parent(Grandparent):

    def home(self):
        print("house")

class Child(Parent):

    def social_media(self):
        print("Social media") 

child_instant = Child()
child_instant.social_media()
child_instant.home()
child_instant.propreties()                       