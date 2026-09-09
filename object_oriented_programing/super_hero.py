class Superhero:

    name = str

    power = str

    universe = str

    def set_superhero(self,name,power,universe):

        self.name = name

        self.power = power

        self.universe = universe

    def get_super_hero(self):

        print(self.name,self.power,self.universe)    

minna_murali_instatnt1 = Superhero()

minna_murali_instatnt1.set_superhero("Minnal Murali","Run,Strenth","Basil_Universe")

minna_murali_instatnt1.get_super_hero()

spider_man_instant1 = Superhero()

spider_man_instant1.set_superhero("Spider men","fly","Marvel")

spider_man_instant1.get_super_hero()