#input = 121

number = 121

original = number

reverse = 0

while number > 0:

    last_digit = number % 10

    reverse = reverse * 10 + last_digit

    number = number // 10

if original == reverse:
    print("Palindrome")

else:
    print("Note palidrome")    
  
