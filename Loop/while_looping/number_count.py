number = int(input("Enter a number"))

count = 0

while number !=0:
     last_digit = number %10

     count = count + 1

     number = number//10

print(count)     

