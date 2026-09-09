'''
### 4. Oxygen Level (SpO2)
- ≥ 95: Normal
- 90 – 94: Mild Concern
- < 90: Critical
'''
oxygen = int(input("Enter Your Oxygen Level"))

if oxygen >= 95:
    print("Normal")

elif oxygen >= 90 and oxygen <= 94: