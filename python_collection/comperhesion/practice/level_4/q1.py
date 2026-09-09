"""
1. Remove leading and trailing spaces Input:[” John “,” Alice
“,” Bob”,“Emma”] Output:[“John”,“Alice”,“Bob”,“Emma”]
"""

names = ["Jhon","","Alice","","Bob","Emma"]

result = [name for name in names if name.strip() ]

print(result)

for name in names:

    if name.strip():

        result.append(name)

   