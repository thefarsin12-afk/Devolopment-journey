"""
8. **Weather Conditions**:
   - Above 30: Hot
   - 20 to 30: Warm
   - Below 20: Cold
"""

weather = int(input("Enter Your Celsius"))

if weather >= 30:
    print("Hot")

elif weather >= 20 and weather < 30:
    print("Warm")

else:
    print("Cold")    