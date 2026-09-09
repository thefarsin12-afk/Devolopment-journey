#select a status_code_num > 2,3,4,5

status_code = int(input("Enter a number..."))

match status_code:
 case 2 :print("Good")

 case 3 :print("Good")

 case 4 :print("Good")

 case 5 :print("Good")

 case _ :print("invalid")