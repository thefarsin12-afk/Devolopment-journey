def is_fibancci_number (number):

    first = 0

    second = 1

    for i in range(number+1):

     next = first + second

     first = second

     second = next

    if next == number:
       
     print(True)

    else:
     print(False)  

is_fibancci_number(5)        