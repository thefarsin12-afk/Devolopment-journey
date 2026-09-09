#child class redefined the method that is already defined in parent class

class Parent:

    def mobile(self):
        print("Redmi note 14")

class Child(Parent):

    def child_mobile(slef):
        print("One plus nord")

child_instants = Child()

child_instants.child_mobile()
            