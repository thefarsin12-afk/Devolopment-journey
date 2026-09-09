#Count Armstrong numbers between a and b.

start = int(input("Enter a number..."))

end = int(input("Enter a number..."))

count = 0

while start <= end:

    original_number = start

    total = 0

    temp = start

    digit = len(str(start))

    while temp !=0:

        last_digit = temp % 10

        total = total + last_digit ** digit

        temp //= 10

    if original_number == total:

        count = count + 1

    start = start + 1

print(count)    