"""
2.  Capitalize every word Input:[“john”,“alice”,“bob”,“emma”]
    Output:[“John”,“Alice”,“Bob”,“Emma”]

"""

names = ["john","alice","bob","emma"] 

reslut = [name.capitalize() for name in names ]

print(reslut)

for name in names:

    reslut.append(name.capitalize())
       