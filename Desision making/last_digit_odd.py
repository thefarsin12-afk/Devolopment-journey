#ck last digit is odd

number=int(input("Enter a number"))
last_digit=number%10
if last_digit%2==0:
    print("Number is even")

else:
    print("Number is note even")    