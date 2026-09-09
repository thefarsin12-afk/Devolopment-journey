"""
Employee id,name,salary,phone,department
        -setemployee(id,name,salary,phone,department)
        -getemployee()
"""

class Employee_id:

    id = int

    name = str

    salary = int

    phone = str

    department = str

    def __init__(self,id,name,salary,phone,department):

        self.id = id

        self.name = name

        self.salary = salary

        self.phone = phone

        self.department = department

    def get_back(self):

        print(self,self.id,self.name,self.salary,self.phone,self.department)   

alex_instant = Employee_id(4398,"Alex",45000,"smasung","Mearn stack devoloper")        
alex_instant.get_back()