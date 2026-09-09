from mysql import connector

class ExpenseListCreateReteiveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(

            user = user,
            password = password,
            host =  "localhost",
            database = "tripwise_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        query = """
             insert into expense(trip,paid_by,amount,category) values(%s,%s,%s,%s) 
                """    
        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Expense has been added")

    def get(self):

        query = """
                select  * from expense
        """    
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        for exp in records:
            print(exp)

    def retrive(self,id=None):

        query = """
               select * from expense where id= %s
        """        
        values = (id,)

        self.cursor.execute(query,values)

        records = self.cursor.fetchone()
        print(records)


    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"=%s,"

        place_holder=place_holder.rstrip(",") # ading amount is %s
        
        query = f"update expense set {place_holder} where id = %s"
        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added")
    
expense_instanse = ExpenseListCreateReteiveUpdateDelete(user="root",password="Password@123")

#expense_instanse.post(trip="kochi",paid_by="cash",amount=3200,category="car")  
#expense_instanse.get()  
#expense_instanse.retrive(id=2)
expense_instanse.put(id=2,amount=5000)    