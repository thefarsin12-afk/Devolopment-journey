#Write a program to find the sum of all even numbers from 1 to n.

def even_number(number):

    sum = 0

    for i in range (1,number +1):

        if i % 2 == 0:

            sum = sum + i

    print(sum) 

even_number(10)           