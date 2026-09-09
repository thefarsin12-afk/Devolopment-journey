from mysql import connector
class SupportListCreateRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None or password==None:
            raise Exception("username and password required")

        self.connection=connector.connect(

            user=user,
            password=password,
            host="localhost",
            database="customer_support_ticket_management_system_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):

        db_colsis=("customer_name","email","subject","description","category","priority","status","assigned_to") 

        difference=set(db_colsis).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference}required")

        colsis=",".join(db_colsis)

        query=f"insert into support_ticket({colsis})values(%s,%s,%s,%s,%s,%s,%s,%s)"

        values=list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()
        print("ticket has been added")

    def get(self):

        query="select * from support_ticket"

        self.cursor.execute(query)

        record=self.cursor.fetchall()

        for t in record:
            print(t)
    def retrieve(self,id=None):

        query="select * from support_ticket where id=%s"

        values=(id,)

        self.cursor.execute(query,values)

        records=self.cursor.fetchone()
        print(records)

    def put(self,id=None,**kwargs):
        # kwargs={customer_name=Vishnu,email=Vishnu@gmail.com,assigned_to=jithin}
        place_holder=""
        for k in kwargs.keys():
            place_holder +=k +"=%s,"
        place_holder=place_holder.rstrip(",")

        query=f"update support_ticket set {place_holder} where id = %s"

        values=list(kwargs.keys())

        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()
        print("record updated.." )

    def filter(self,**kwargs):

        #kwargs={status="pending","priority":"high"}
        
        place_holder=""

        for k in kwargs.keys():

            place_holder +=k+ "=%s and"

        place_holder =place_holder.rstrip("and ")

        query=f"select * from support_ticket where {place_holder}"

        values=list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:
            for t in records:
                print(t)
        else:
            print("No records")

    def summary(self):

        query="select status,count(*) as count from support_ticket group by status"

        self.cursor.execute(query)

        response=self.cursor.fetchall()

        priority_summary_query="select priority ,count(*) as count from support_ticket group by priority"

        self.cursor.execute(priority_summary_query)

        p_response=self.cursor.fetchall()
        print("p_response",p_response)
        print(response)

ticket_instance=SupportListCreateRetrieveUpdateDelete(user="root",password="Password@123")

ticket_instance.post(customer_name="Meera",
                    email="meera@gmail.com",
                    subject="Payment deducted but order pending",
                    description="I made the payment yesterday but my order is still showing pending",
                    category="payment",
                    priority="low",
                    status="colsed",
                    assigned_to="open")

#ticket_instance.get()

#ticket_instance.retrieve(id=2)

#ticket_instance.put(id=2,customer_name="Vishnu",email="Vishnu@gmail.com",assigned_to="jithin")

#ticket_instance.filter(customer_name="arun")

ticket_instance.summary()
print(ticket_instance)