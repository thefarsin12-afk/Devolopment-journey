def fibbnacci_number(number):

    first = 0

    second = 1

    for count in range(number):

        print(first)
        

        next = first + second

        first = second

        second = next

fibbnacci_number(8)    

