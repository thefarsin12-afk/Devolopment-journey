#Find the difference between the last two Fibonacci numbers generated up to n.

number = int(input("Enter a number..."))

first = 0

second = 1

defrense = 0

while first <= number:

    defrense = first

    next_number = first + second

    first = second

    second = next_number

print(defrense - first)       