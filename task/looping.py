"""
1. Print Numbers
Print numbers from 1 to 10 using a while loop.
"""

number = 1

while number <=10:
    print(number)
    number = number + 1

"""
2. Sum of First N Numbers
Input a number n and print the sum of numbers from 1 to n.
Example:
Input: 5
Output: 15
"""    
print("sum")

total = 0
number = 1
n = 5

while number <= n :

    total = total + number
    number = number + 1

print(total)

"""
3. Reverse a Number

Reverse the digits of a number using a while loop.

Example:

Input: 1234
Output: 4321
"""

def reverse_number(number):

    reverse = 0
    
    while number != 0:

        last_digit = number % 10

        reverse = reverse * 10 + last_digit

        number = number // 10

    print(reverse)

reverse_number(1234)        

"""
4. Count Digits

Count the number of digits in an integer.

Example:

Input: 98765
Output: 5
"""


def digit(number):
 
 count = 0

 while number != 0:

    count = count + 1

    number = number // 10

 print(count)

digit(987658)        

"""
5. Palindrome Number

Check whether a number is a palindrome.

Example:

Input: 121
Output: Palindrome
"""

def palindrome_number(number):

   reverse = 0
   original_number = number

   while number != 0:

      last_digit = number % 10

      reverse = reverse * 10 + last_digit

      number = number // 10

   if original_number == reverse:
         print("palidrome ")

   else:print("not palidorme")

palindrome_number(121)        

"""
6. Multiplication Table
Print the multiplication table of a given number.
Example:
Input: 5
Output:
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
"""

def multiplication_tabile(number):

    product = 1

    for i in range(1 , 10 +1):

        product = number *i

        print(f"{i}*{number} = {product}") 

multiplication_tabile(5)           

"""
7. Factorial

Find the factorial of a number using a for loop.

Example:

Input: 5
Output: 120
"""



def facotrial_number (number):

    facotrial = 1

    for i in range (1,number +1):

        facotrial = facotrial * i

    print(facotrial)

facotrial_number(5)

"""
8. Prime Number

Check whether a number is prime using a for loop.
"""

def prime_number (number):

    if number <= 1:
        print("Not prime number")
        return


    for i in range(2,number):

        if number % i == 0:
            print("Not prime number")
            break

    else:
        print("Prime number")    

prime_number(-7)        

"""
9. Fibonacci Series

Print the first n Fibonacci numbers.
"""

def fibanacci_seires(number):

    first = 0

    second = 1

    for i in range (1,number +1):

     print(first)
        
     next_number = first + second

     first = second

     second = next_number

fibanacci_seires(7)


"""
10. Armstrong Number

Check whether a number is an Armstrong number.

Example:

Input: 153
Output: Armstrong Number
"""

def armstrong_number(number):

    count = 0

    temp = number

    original_number = number

    total = 0

    digit = len(str(number))

    while number != 0:

        last_digit = number % 10

        total = total + last_digit ** digit

        temp = temp // 10

    if original_number == total:
        print(original_number)
        count = count + 1

    print("Total armstron number is ",count)    

armstrong_number(1000)            
        
