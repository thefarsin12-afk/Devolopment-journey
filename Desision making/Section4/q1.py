#1. **Positive Number – Even or Odd**
#- Check if positive. If yes, check for even/odd. 
#Else, state "Not a positive number."

number = int(input("Enter a number"))

if number > 0:
    print("Number is positive")

    if number %2 ==0:
        print("Number is even")

    else:
        print("Number is odd")    

else:
    print("Number is note positive")