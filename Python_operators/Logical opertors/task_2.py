year=int(input("Enter a year"))
value=(year %100!=0 and year%4==0) or (year % 100==0 and year%400==0)
print(value)