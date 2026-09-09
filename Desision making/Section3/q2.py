# **BMI**: < 18.5 (Underweight), 18.5 – 24.9 
# (Normal), 25 – 29.9 (Overweight), ≥ 30 (Obese)

body_weight_kg = int(input("Enter your Weight"))

body_height_cm = int(input("Enter your Height"))

height_in_meter = body_height_cm/100

bmi = body_weight_kg / height_in_meter **2

if bmi < 19:
    print("Under weight")

elif bmi >= 19 and bmi <=25:
    print("Normal") 

elif bmi >=25 and bmi <=30:
    print("Overweight")

else:
    print("Obese")      