"""
### 2. Blood Pressure (Systolic)
- < 120: Normal
- 120 – 129: Elevated
- 130 – 139: High BP Stage 1
- ≥ 140: High BP Stage 2
"""

blood_pessure = int(input("Enter Your BP"))

if blood_pessure <= 120:
    print("Normal")

elif blood_pessure > 120 and blood_pessure <= 129:
    print("Elevated")

elif blood_pessure > 130 and blood_pessure < 139:
    print("High BP Stage 1")

else:
    print("High BP Stage 2")       