number = int(input("Enter a number"))

def fibanoc_number(number):

    first = 0

    second =1

    for count in range(number+1):

        print(first)

        next_number = first + second

        first = second

        second = next_number

fibanoc_number(number)            
