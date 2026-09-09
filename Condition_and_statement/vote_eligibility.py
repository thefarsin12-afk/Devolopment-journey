#Write a program to check whether a person is eligible to vote (age ≥ 18).

db_age = 18

db_adhar ="YES"

print("Check your voting eligibility")

age = int(input("Enter Your Age...."))

if age == db_age:
     
     adhar = input("You have adhar card...YES/NO")
     
     if adhar == db_adhar:

      print("Youre eligile")

      print(f"Verified Age = {db_age},Adhar card = {db_adhar}")

     else:
         print("Youre note eligible")

else:
     print("Youre note elgibile")