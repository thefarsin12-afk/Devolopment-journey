#3. **Age Group**: < 13 (Child), 
# 13 – 19 (Teen), 20 – 59 (Adult), ≥ 60 (Senior)

age = int(input("Enter Your Age"))

if age < 13:
    print("Child")

elif age >= 13 and age <=19:
    print("Teen")

elif age >= 20 and age <=59:
    print("Adult")        

else:
    print("Senior")    