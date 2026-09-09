number = int(input("Enter an number...."))

dumb = number

total = 0

while dumb > 0:

    last_digit = dumb % 10

    total = total + last_digit**3

    dumb = dumb // 10

if total == number:
    print(f"Armstring Number = {total}")

else:
    print("Note armstring number")       