class Parent:

    def house(self):

        print("House")

class Child(Parent):

    def social_media(self): 

        print("Social_media")   

house_instance1= Parent()

house_instance1.house()

social_media = Child()

social_media.social_media()

social_media = Parent()
social_media.house()