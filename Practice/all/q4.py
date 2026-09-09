"""
5. Find the Sum of the Odd Digits.
Example:
Input: 58392
Output: 17
Explanation:
5 + 3 + 9 = 17
"""
def sum_odd(number):

    sum = 0

    while number != 0:

        last_digit = number % 10

        if last_digit % 2 != 0:
            
            sum = sum + last_digit

        number = number // 10

    print(sum)

sum_odd(58392)            