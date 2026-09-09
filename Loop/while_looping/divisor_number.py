#q3)scenario: divisors of number 8  o/p {1,2,4,8}

number = 8

check = 1

while check <= number:

    if number % check == 0:
        print(check)

    check = check + 1
