
def odd_number():

 number =int(input("Enter a number"))
 while number !=0:
        
        digit = number % 10

        if digit % 2 !=0:

            print(number)
            break

        else:
            number = number // 10
odd_number()
           
   
    

            

        
