"""
3. Find the Product of the Digits.
Example:
Input: 1234
Output: 24
Explanation:
1 × 2 × 3 × 4 = 24
"""

def product_number(number):

    product = 1

    while number != 0:

        last_digit = number % 10

        product = product * last_digit

        number = number // 10

    print (product)

product_number(1234)        