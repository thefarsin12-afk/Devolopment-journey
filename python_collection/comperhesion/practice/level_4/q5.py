"""
5.  Replace spaces with underscores Input:[“Python Basics”,“Learn
    Django”,“React Course”]
    Output:[“Python_Basics”,“Learn_Django”,“React_Course”]
"""

charaters = ["Python Basics,","Learn Django","React Course"]

result = [ch.replace(" ","_") for ch in charaters]

print(result)

for ch in charaters:

    result.append(ch.replace(" ","_"))
    