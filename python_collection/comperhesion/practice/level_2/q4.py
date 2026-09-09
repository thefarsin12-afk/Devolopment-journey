"""
4.  Extract names starting with ‘A’ Input:
    names=[“Alice”,“Bob”,“Andrew”,“Emma”,“Alex”] Expected Output:
    [“Alice”,“Andrew”,“Alex”]
"""

names = ["Alice","Bob","Andrew","Emma","Alex"]

result = [name for name in names if name.startswith("A") ]

print(result)

for name in names:

    if name.startswith("A"):

        result.append(name)

      