# identify min or max

num1 = int(input("Enter a number...."))

num2 = int(input("Enter a number...."))

option = (input("Enter Option Min or Max"))

match option:
 
 case "min":
      if num1<num2:
         print("Minimum number is",num1)

      else:
         print("Minimum number is",num2)       

 case "max":
      if num1>num2:
         print("Maiximum number is",num1)

      else:
         print("Maximum number is",num2)   
      
 case _:print("Invalid")