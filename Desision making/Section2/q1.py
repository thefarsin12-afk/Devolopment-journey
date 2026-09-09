"""
### 1. Blood Sugar
- < 100: Normal
- 100 – 125: Prediabetes
- ≥ 126: Diabetes
"""

sugar = int(input("Enter Your Sugar Value"))

if sugar < 100:
    print("Normal") 

elif sugar >= 100 and sugar <=125:
    print("Pre Diabetes")

else:
    print("Diabetes")
