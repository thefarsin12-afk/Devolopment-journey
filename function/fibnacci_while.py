def fabnicc_number(number):

    first = 0

    second = 1

    while first <= number:

        if first == number:

            print ("Fibnicc number")

            break

        next = first + second

        first = second

        second = next

    else:
        print("Note a fibonacci number")        

fabnicc_number(25)        