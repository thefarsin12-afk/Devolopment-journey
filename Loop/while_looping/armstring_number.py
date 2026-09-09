number = int(input("Enter a number: "))
original_number = number
digit_count = len(str(number))
total = 0

while number != 0:
    last_digit = number % 10
    total = total + last_digit ** digit_count
    number = number // 10

if total == original_number:
    print("Armstrong number")
else:
    print("Not Armstrong number")
