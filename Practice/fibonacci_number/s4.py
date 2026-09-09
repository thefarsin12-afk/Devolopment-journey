#Find the sum of all even Fibonacci numbers up to n.

number = int(input("Enter a number"))

first = 0

second = 1

total = 0

while first <= number:
     
     if first % 2 ==0:
          
      total += first

     next_number = first + second

     first = second

     second = next_number

print(sum)       