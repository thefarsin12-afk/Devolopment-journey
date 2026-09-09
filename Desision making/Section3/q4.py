#**Cholesterol**: < 200 (Desirable), 200 – 239 (Borderline), ≥ 240 (High)

cholesterol = int(input("Enter Your Cholesterol Value"))

if cholesterol <= 200:
    print("Desirable")

elif cholesterol > 200 and cholesterol <= 239:
    print("Borderline")

else:
    print("High")    