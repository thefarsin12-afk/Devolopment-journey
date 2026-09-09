def is_prime_number(number):

    is_prime = True

    for i in range(2 , number):

        if number % i == 0:

            is_prime =False
            break

    if is_prime:
            
        print(f"Prime Number {number}")
        
    else:
        print(f"Note Prime Number {number}")

is_prime_number(8)                     

