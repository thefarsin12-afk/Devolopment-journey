'''
### 7. Daily Steps
- < 5000: Sedentary
- 5000 – 9999: Moderately Active
- ≥ 10000: Active
'''
step = int(input("Enter your daily steps"))

if step <= 5000:
    print("Sedentary")

elif step > 5000 and step <=9999:
    print("Moderately Active") 

else:      
    print("Active")