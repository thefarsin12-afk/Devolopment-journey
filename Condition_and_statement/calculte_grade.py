"""
Write a program to calculate the grade based on marks.
90–100 → A
80–89 → B
70–79 → C
40–69 → D
Below 40 → Fail
"""
print("Check Youre Grade")

mark = int(input("Enter your mark...."))

if mark >=90 and mark <100:
    print("A")

if mark<0 or mark >100:
        print("Inavlid")

elif mark >=80 and mark <=89:
    print("B")

elif mark >=70 and mark <=79:
    print("C")    

elif mark >=40 and mark <=69:
    print("D")    

else:
    print("F")    

