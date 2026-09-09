"""
*Leap Year**: Check if a given year is a leap year.
"""

leap_year = int(input("Enter Year"))

if leap_year % 400 == 0:
    print("Leap Yaer")

elif leap_year % 100 == 0:
    print("Note a Leap Year")

elif leap_year % 4 ==0:
    print("Leap Year")

else:
    print("Note a leap year")            