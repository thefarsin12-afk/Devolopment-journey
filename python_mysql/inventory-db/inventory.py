from mysql import connector

class CreateListRetrieveUpdateDelete:

    def __init__(self,user = None , password = None):

        self.connection = connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database =" inventory_db"
        )

        self.cursor = self.connection.cursor()


    def post(self,**kwargs):

        db_cloum = ("product_name","category","quantity","price")

        deffrence = set(db_cloum).difference(kwargs)

        if deffrence:

            raise Exception(f"{deffrence}required")

        colsis=",".join(db_cloum)

        query = f"insert into inventory_({colsis}) values(%s,%s,%s,%s)"
        values = list(kwargs.values())    

        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added")

    def get(self):

        query = "select * from inventory_"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for k in record:
            print(k)    

    def retrieve(self,id=None):

        query = "select * from inventory_ where id = %s"

        values = (id,)

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()
        print(record)

    def put(self,id=None,**kwargs):

        
        place_holder = "" 

        for k in kwargs.keys():
            place_holder +=k+"=%s,"

        place_holder = place_holder.rstrip(",")    

        query = f"update inventory_ set {place_holder} where id=%s"

        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")

    def delete(self,id=None):

        query = "delete from inventory_ where id=%s"

        values = (id,)

        self.cursor.execute(query,values)

        self.connection.commit()
        print("record hass been deleted")   

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder +=k+"=%s and"

        place_holder = place_holder.rstrip("and ")

        query = f"select * from inventory_ where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        record = self.cursor.fetchall()

        if record:

            for k in record:
                print(k)

        else:print("no records")      


inventory_instance = CreateListRetrieveUpdateDelete(user="root",password="Password@123")            
#inventory_instance.post(product_name="Head_phone",category="Electronics",quantity= 12,price= 1298)
#inventory_instance.get()
#inventory_instance.retrieve(id=2)
#inventory_instance.put(id=1,quantity=11,price=599)
#inventory_instance.delete(id=3)
#inventory_instance.filter(category="Electronics")