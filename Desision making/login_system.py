#create a login sysytem user name and password

user_name="thefarsii"
user_password=1234

name=(input("Enter user name"))

if name==user_name:
   password=int(input("Enter password"))

   if password == user_password:
     print("Login Succefully")

   else:
      print("Inavalid password")
else:
   print("Inavalid user name")      
 