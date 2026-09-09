# add/create = post
# list:all = get
# detail = retrieve
# update = put
# remowe = delete

class DietLense:

    def __init__(self):
        
        self.food_logs=[

            {"id":1,"name":"dosa","calorie":180,"owner":"hari"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","name","calorie","owner"}

        """for field in required_fields:

            if field not in kwargs:

                raise Exception("Is missing")"""


        missing_field = required_fields.difference(kwargs.keys())

        if missing_field:

            raise ValueError(missing_field,"Is missing error")



        self.food_logs.append(kwargs)

        print("food log has been added")    

    def get(self):

        if len(self.food_logs) ==0:
            print("No found")

        else:

            for log in self.food_logs:
                print(log)        

    def retrive(self,id=None):         

        if not id:
            raise ValueError("is missing")

        else:
            return [log for log in self.food_logs if log.get("id")==id]  
        
#id none using default value

    def put(self,id=None,**kwargs):

        logs = [logs for logs in self.food_logs if logs.get("id")==id][0] 

        logs.update(kwargs)

        print("Record has been updated")    
        print(logs)    

    def delete(self,id=None):

        logs = [log for log in self.food_logs if log.get("id")==id][0]

        self.food_logs.remove(logs)
        print("Id has been removed")
        self.get()
        

deit_instance = DietLense()
deit_instance.post(id=2,name="alex",calorie=174,owner="jhon") 
"""deit_instance.get()       
print(deit_instance.retrive(id=2))
deit_instance.put(id=1,name="porotta")"""
deit_instance.delete(id=1)

"""expense_dictionary = {"id":1,"title":"electrecity_bill","amount":5786,"category":"bills","owner":"hari"}

data = {"title":"KSEB Bill","amount":6000}

expense_dictionary.update(data)

print(expense_dictionary)
"""