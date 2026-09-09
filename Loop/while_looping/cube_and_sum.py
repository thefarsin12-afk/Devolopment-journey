number = int(input("Enter a number"))

total =0

while number !=0:
    last_digit = number %10

    cube = last_digit **3

    total = total + cube

    number=number//10

    print(total) 