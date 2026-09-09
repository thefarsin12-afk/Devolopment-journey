number =int(input("Enter a number"))

def armstrong_number(number):

    total = 0

    orginal = number

    digit_count = len(str(number))

    while number != 0:
    
     last_digit = number % 10

     total = total + (last_digit ** digit_count)

     number = number // 10

    if total == orginal:

        print (f"Arm strong number{total}")     
        
    else:    
        print (f"Note Arm strong number") 

armstrong_number(number)           

