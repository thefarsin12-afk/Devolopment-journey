#Input: 98765
#Output: 5

number = 98765

total = 0

while number != 0:

    last_digit = number % 10

    total = total + 1

    number =  number // 10

print(total)    