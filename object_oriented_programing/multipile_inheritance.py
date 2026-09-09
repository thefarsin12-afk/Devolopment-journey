# a child class handiling to multiple parent class

class Father:

    def cricket_skill(self):
        print("Cricket skill")

class Mother:

    def dancing_skill(self):
       print ("Dancing skill") 

class Child(Father,Mother):

    def coding_skill(self):
       print ("Coding skill")

child_instant = Child()
child_instant.coding_skill()
child_instant.cricket_skill()
child_instant.dancing_skill()        

                       