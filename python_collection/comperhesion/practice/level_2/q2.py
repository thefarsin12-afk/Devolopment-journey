"""
2.  Extract words longer than 5 letters Input:
    words=[“apple”,“watermelon”,“dog”,“elephant”,“cat”] Expected Output:
    [“watermelon”,“elephant”]
"""
words=["apple","watermelon","dog","elephant","cat"]

output = []

for w in words:

    if len(w) > 5:
        output.append(w)

print(output)        