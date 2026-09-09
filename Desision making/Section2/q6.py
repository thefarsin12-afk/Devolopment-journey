'''
### 6. Stress Level (1-10)
- 1 – 3: Low Stress
- 4 – 6: Moderate Stress
- 7 – 10: High Stress
'''

stress = int(input("Enter your stress level"))

if stress >= 1 and stress <= 3:
    print("Low Stress")

elif stress >= 4 and stress <= 6:
    print("Moderate Stress") 

else:
    print("High Stress")       
