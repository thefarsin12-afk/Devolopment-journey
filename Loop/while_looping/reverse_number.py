#q4)scenario: reverse number 123 o/p{321}

number =123

reverse = 0

while number > 0:
    last_digit = number %10

    reverse = reverse * 10 + last_digit

    number = number // 10

print(reverse)