from mysql import connector

class IssuePostGetRetrievePutDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database="road_issue_db"
        )
        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        query = "insert into issue_(title,location,posted_by,status) values(%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        self.connection.commit()
        print("Record hass been added")

    def get(self):
            
            query ="select * from issue_"

            self.cursor.execute(query)
            record = self.cursor.fetchall()

            for issue in record:
                 print(issue)

    def retrieve(self,id=None):

         query = "select * from issue_ where id = %s"
         values = (id,)

         self.cursor.execute(query,values)
         record = self.cursor.fetchone()
         print(record)

    def put(self,id=None,**kwargs):
        place_holder = ""
        for k in kwargs.keys():
              place_holder +=k+"=%s,"    
        place_holder = place_holder.rstrip(",")     
        query =f"update issue_ set {place_holder} where id= %s"
        values = list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()  
        print("issue has been added")

    def delete(self,id=None):

         query = """delete from issue_ where id=%s"""
         values = (id,)

         self.cursor.execute(query,values)
         self.connection.commit()
         print("recored removed")    
         

issue_instance = IssuePostGetRetrievePutDelete(user="root",password="Password@123") 
#issue_instance.post(title="Damaged Road Near Bus Stand",location="Valanchery",posted_by="adham",status="unsolved")
#issue_instance.get()
#issue_instance.retrieve(id=2)
#issue_instance.put(id=1,title="Broken Road",posted_by="aliyar")
#issue_instance.delete(id=1)