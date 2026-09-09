#2.Convert all names to uppercase Input:
#names=[“john”,“alice”,“bob”,“emma”] Output:
#[“JOHN”,“ALICE”,“BOB”,“EMMA”]

names = "jhon","alice","bob","emma"

upper_case = [name.upper() for name in names]
print(upper_case)

for name in names:

 upper = name.upper()

 upper_case.append(upper)

print(upper_case) 