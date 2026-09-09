#Write a program to find the largest of three numbers.

num1 = int(input("Enter a number..."))

num2 = int(input("Enter a number..."))

num3 = int(input("Enter a number..."))

if num1 > num2 and num1 > num3:
    print(f"Greater Number = {num1}")

elif num2>num1 and num2>num3 :
    print(f"Greater Number = {num2}")

elif num3>num1 and num3>num2:
    print(f"Greater number = {num3}")

elif num1==num2 and num2==num3:
    print("Numer are equal")

else:
    ("invalid...")    