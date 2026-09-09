"""
5.  Label numbers Input:[50,120,80,200,95]
    Output:[“Low”,“High”,“Low”,“High”,“Low”]
"""

label_number = [50,120,80,200,95]

result = ["high" if num >= 100 else "Low" for num in label_number]

print(result)

for num in label_number:

    if num >= 100:
        result.append("High")
        

    else:
        result.append("Low")
        
        