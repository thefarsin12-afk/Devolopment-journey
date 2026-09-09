#sum of dgit

def sum_of_digit(number):

    sum =0

    while number !=0:

        last_digit = number % 10

        sum = sum + last_digit

        number = number // 10

    print(sum)

sum_of_digit(164)    