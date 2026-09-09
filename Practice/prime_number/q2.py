#Check whether a number is Prime.

def prime(number):

    is_prime = True

    if number <= 1:

        print("Nute Prime Number")
        return

    for i in range(2 , number):

        if number % i == 0:

            is_prime = False
            break

    if is_prime:
        print("Prime Number")

    else:
        print("Note Prime Number")        

prime(7)        