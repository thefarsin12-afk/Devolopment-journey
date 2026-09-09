#Write a program to check whether a year is a leap year.

print("Check Leap Year")

year =int(input("Enter a year"))

if (year % 100 ==0 and year % 400 ==0) or year % 100 !=0 and year  % 4 ==0:

    print(f"{year} Leap Year")

else:
    print(f"{year} Is note leap year")    