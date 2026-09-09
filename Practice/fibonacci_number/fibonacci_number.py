#Print the first n Fibonacci numbers.
number = int(input("Enter a number"))

def fibanacci_number():

    first = 0

    second = 1

    for i in range (number):

     print(first)
     
     next_number = first + second

     first = second

     second = next_number

fibanacci_number()
    