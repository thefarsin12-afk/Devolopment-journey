# checking key,including dictionary,otherwise using try,exept,finally errorr handling method.

employee = {"id":100 , "name":"shyam","dept":"hr"}

key = input("enter key")

try:

    print(employee[key])

except Exception as e:

    print(e)     

finally:

    print("db commit")    


