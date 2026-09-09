"""
**Student Grading**:
   - Marks ≥ 90: Grade A
   - Marks ≥ 75: Grade B
   - Marks ≥ 50: Grade C
   - Otherwise: Fail
"""

grade = int(input("Enter Your Score"))

if grade > 90:
    print("A Grade")

elif grade > 75:
    print("B Grade")

elif grade > 50:
    print("C Grade")

else:
    print("Fail")        