#Find the GCD of 10 and 20 using a for loop.

number1 = 10

number2 = 20

if number1 < number2:

   smaller = number1

else:
    smaller = number2

gcd = 1

for i in range (1, smaller + 1):

    if number1 % i == 0 and number2 % 1 == 0:
        gcd + i

print(gcd)        