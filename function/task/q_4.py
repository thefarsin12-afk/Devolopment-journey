def reverse_number(number):

    total = 0

    while number !=0:
        
        last_digit = number % 10 
        
        print(last_digit)

        number =number // 10  


reverse_number(400)       
reverse_number(123)       