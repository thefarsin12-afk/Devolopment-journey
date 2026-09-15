#7. Find the sum of numbers from 1 to n.

def sum_numbers(number):

    sum = 0

    for i in range(1,number + 1):

        sum = sum + i

    print(sum)

sum_numbers(5)        