"""
#number 4 factorial 24

number = 4

factorial =1

while number >= 1:

    factorial = factorial * number

    number = number - 1

print(factorial)    

"""

number = (int(input("Enter anumber")))

i = 1

product = 1

while i <= number:

    product = product*i

    i=i + 1

print(f"factorial number {number} ={product}")    