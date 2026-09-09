class Gym_workout:

    chest = str

    set_1 = int

    rep_1 = int

    back = str

    set_2 = int

    rep_2 = int

    biceps = str

    set_3 = int

    rep_3 = int

    triceps = str

    set_4 = int

    rep_4 = int

    shoulder = str

    set_5 = int

    rep_5 = int

    abs = str

    set_6 = int
    
    rep_6 = int

    leg = str

    set_7 = int
    
    rep_7 = int

    def __init__(self,chest,set_1,rep_1,back,set_2,rep_2,biceps,set_3,rep_3,
      triceps,set_4,rep_4,shoulder,set_5,rep_5,abs,set_6,rep_6,leg,set_7,rep_7):

        self.chest = chest

        self.set_1 = set_1

        self.rep_1 = rep_1

        self.back = back

        self.set_2 = set_2

        self.rep_2 = rep_2

        self.biceps = biceps

        self.set_3 = set_3

        self.rep_3 = rep_3

        self.triceps = triceps

        self.set_4 = set_4

        self.rep_4 = rep_4

        self.shoulder = shoulder

        self.set_5 = set_5

        self.rep_5 = rep_5

        self.abs = abs

        self.set_6 = set_6

        self.rep_6 = rep_6

        self.leg = leg

        self.set_7 = set_7

        self.rep_7 = rep_7

    def print_split(self):

        print(self,self.chest,self.set_1,self.rep_1,self.back,self.set_2,self.rep_2,self.biceps,self.set_3,self.rep_3,self.triceps,self.set_4,self.rep_4,self.shoulder,self.set_5,self.rep_5,
              self.abs,self.set_6,self.rep_6,self.leg,self.set_7,self.rep_7)    

workout_split_instant = Gym_workout("Bench Press",4,12,"Lat pulldown",3,15,"One by one",3,12,"Skull crusher",3,12,"Dumbell head ower",4,8,"Crunches",4,20,"Squat",4,8)
workout_split_instant.print_split()
        