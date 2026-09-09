sugar=int(input("Enter your value"))

if sugar>300:
    print("Dangerous High")

elif sugar>140 and sugar<=220:
    print("High")

elif sugar>90 and sugar<=140:
    print("Normal")

elif sugar>80 and sugar<=90:
    print("Low")

else:
    print("Dangerous Low")           
