#. **Body Temp (°C)**: < 36 (Low), 36 – 37.5 (Normal), > 37.5 (Fever)

body_temp = int(input("Enter your Body Temperature"))

if body_temp <= 36:
    print("Low")

elif body_temp > 36 and body_temp <=37.5:
    print("Normal")

else:
    print("Fever")        