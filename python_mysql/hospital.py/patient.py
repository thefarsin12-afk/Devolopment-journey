from mysql import connector

class CreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection =  connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database = "hospital_db"
        )

        self.cursor = self.connection.cursor()

#Register a new patient visit record
    def post(self,**kwargs):

        db_cloum = ("patient_name","phone_number","assigned_doctor","department","appointment_date","status","consultation_fee")    

        deffrence = set(db_cloum).difference(kwargs)

        if deffrence:
            raise Exception (f"{deffrence} requred")

        colsis = ",".join(db_cloum)

        query = f"insert into patients({colsis}) values(%s,%s,%s,%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record has been added")

#- View all registered patient visits

    def get(self):

        query = "select * from patients"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for k in record:
            print(k)        

#Update appointment status (`Pending`, `Completed`, `Cancelled`) or assigned doctor

    def put(self,patient_id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update patients set {place_holder} where patient_id=%s" 

        values = list(kwargs.values())
        values.append(patient_id)

        self.cursor.execute(query,values)

        self.connection.commit()
        print("updated")   

#Delete duplicate or erroneous patient entries  

    def delete (self,patient_id=None) :

        query = "delete from patients where patient_id=%s"

        values = (patient_id,)

        self.cursor.execute(query,values)
        self.connection.commit()
        print("Record deleted")   

#Filter patients by status or department

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"=%s and"

        place_holder = place_holder.rstrip("and ")   

        query =f"select * from patients where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        record = self.cursor.fetchall()

        if record:
            for k in record:
                print(k)

        else:print("no record") 

#Calculate total consultation fees collected

    def fees(self):

        query = "select sum(consultation_fee) from patients"

        self.cursor.execute(query)

        record = self.cursor.fetchone()

        print("Total = ",record)

#Count total appointments per doctor

    def total(self):

        query = "select assigned_doctor,count(*) as total from patients group by assigned_doctor"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        print(record)         


hospital_instance = CreateListRetrieveUpdateDelete(user="root",password="Password@123") 

"""hospital_instance.post( patient_name="Faisal Ahmed",
                        phone_number="9988776655",
                        assigned_doctor="Dr. Priya",
                        department="Orthopedics",
                        appointment_date="2026-09-15",
                        status="Completed",
                        consultation_fee=1000.00)  """ 

#hospital_instance.get()

#hospital_instance.put(patient_id=2,status="Completed")

#hospital_instance.delete(patient_id=4)

#hospital_instance.filter(status="Completed")

#hospital_instance.fees()

hospital_instance.total()

