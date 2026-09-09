#Print the Fibonacci numbers in reverse order (first n numbers).

number = int(input("Enter a number"))

first = 0

second =  1

reverse = 0

while first <= number:
 
  last_diit = first % 10

  reverse *= 10 + first

  number //= 10

  next_number = first 

  first = second

  second = next_number

print(reverse)

  # undertand list # reverse fibonicci series
  