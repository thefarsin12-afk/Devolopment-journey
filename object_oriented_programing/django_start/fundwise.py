#FundWise user has to add,list,detail,update,delete his daily expense   

class Fundwise:

    def __init__(self):

        self.daily_expense = [

            {"id":1,"title":"travel","amount":200,"category":"cash","owner":"chikumon"}
        ]

#create or add (post)
    def post(self,**kwargs):

        requirement_fields = {"id","title","amount","category","owner"}

        missing_feild = requirement_fields.difference(kwargs)

        if missing_feild:

            raise ValueError(missing_feild,"is missing") 

        self.daily_expense.append(kwargs)

        print("Daily expence has been added")

#all list (get)
    def get(self):

        print(self.daily_expense)    

#details (retrieve)

    def retrieve(self,id):

        for expence in self.daily_expense:    

            if expence ["id"] == id:
                print(expence)  
                return

        print("Expence no found")    

#put
    def put(self,id,**kwargs):

        for expence in self.daily_expense:

            if expence ["id"] == id:
                expence.update(kwargs)
                print(self.daily_expense)
                return

        print("Expence not found")    

#delete

    def delete(self,id):

        for expence in self.daily_expense:

            if expence["id"] == id:
                self.daily_expense.remove(expence)
                print(self.daily_expense)
                return

        print("Expence not found")   

                 

         

daily_expence_instant = Fundwise()
daily_expence_instant.post(id=2,title="food",amount=150,category="upi",owner="ali")
daily_expence_instant.get()
daily_expence_instant.retrieve(id=2)
daily_expence_instant.put(2,amount=300)
daily_expence_instant.delete(1)

