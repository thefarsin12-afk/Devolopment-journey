#Check whether a number is an Armstrong number.

number = int(input("EWnter a number..."))

original_number = number

digit_count = len(str(number))

total = 0

while number != 0:

    last_digit = number % 10

    total = total + last_digit ** digit_count

    number = number // 10

if original_number == total:
    print("Armstrong Number")

else:print("Not Armstrong Number")        