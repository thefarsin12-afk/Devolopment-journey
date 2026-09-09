number = int(input("Enter a number"))
cube=0

while number !=0:

    last_digit = number % 10
  
    cube = last_digit ** 3

    number=number//10

    print(cube)