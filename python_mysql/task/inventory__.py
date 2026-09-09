from mysql import connector

class CreateListRetrieveUpdateDelete:

    def __init__(self,user = None,password = None):

        self.connection = connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database = "inventory__db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_cloums = ("item_name","sku","category","quantity","reorder_level","unit_price","storage_zone","status",)   

        deffrence = set(db_cloums).difference(kwargs)

        if deffrence:
            raise Exception(f"{deffrence} required")

        colsis = ",".join(db_cloums)

        query = f"insert into inventory({colsis}) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()
        print("Record has been added")

    def get(self,id=None):

        query = "select * from inventory"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for k in record:
            print(k)

#Search for a patient by phone number or name
    
#Update appointment status (`Pending`, `Completed`, `Cancelled`) or assigned doctor

    def put(self,item_id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update inventory set {place_holder} where item_id=%s "

        values = list(kwargs.values())
        values.append(item_id)

        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")    

#Delete duplicate or erroneous patient entries

    def delete(self,id=None):

        query = "delete from inventory where item_id=%s"
        values =(id,)

        self.cursor.execute(query,values)
        self.connection.commit()
        print("record hass benn deleted")

#Filter patients by status or department
   
    def filter(self,**kwargs):

        place_holder=""

        for k in kwargs.keys():
            place_holder +=k+"=%s and"

        place_holder = place_holder.rstrip("and ")

        query = f"select * from inventory where {place_holder}" 

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        record = self.cursor.fetchall()

        if record:
            for k in record:
                print(k)

        else:print("no records")    

#Calculate total unit_price  collected

    def total(self):

        query = "select quantity,sum(quantity) as total from inventory group by unit_price" 

        self.cursor.execute(query)

        responce = self.cursor.fetchall()
        print(responce)     

#Count total item_name per quantity

    def total_quantity(self):

        query = "select item_name,count(*) as total from inventory  group by item_name"

        self.cursor.execute(query)

        record = self.cursor.fetchall()
        print(record)
                   

inventory_instants = CreateListRetrieveUpdateDelete(user="root",password="Password@123")
"""inventory_instants.post(
    item_name="Surgical Gloves",
    sku="MED002",
    category="Medical Equipment",
    quantity=50,
    reorder_level=10,
    unit_price=25.00,
    storage_zone="Zone-B",
    status="In Stock"
)"""

#inventory_instants.get(id=1)
#inventory_instants.put(item_id=2,status="Completed")
#inventory_instants.delete(id=2)
#inventory_instants.filter(status="Pending")
#inventory_instants.total()
inventory_instants.total_quantity()