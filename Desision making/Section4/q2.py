'''
2. **Driving License Eligibility**
   - Age ≥ 18: Ask if test passed (yes/no).
   - Yes: "License Approved" | No: "Test not cleared."
   - Age < 18: "Not eligible due to age."
'''
age = int(input("Enter your age"))

if age >= 18:
    exam_verify=input("Do you have passed exam yes/no")

    if exam_verify == "yes":
        print("Licenese Approved")

    else:
        print("Test not cleared")    

else:
    print("Your not eligible for licence")        