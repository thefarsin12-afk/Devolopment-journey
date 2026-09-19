#Write a Python program to reverse an integer using a while loop.

def reverse(number):

    reverse = 0

    while number > 0:

        last_digit = number % 10

        reverse = reverse * 10 + last_digit

        number = number // 10

    print(reverse)

reverse(4001)        