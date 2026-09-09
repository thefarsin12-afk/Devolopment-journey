"""
3.  Pass or Fail Input:[35,70,90,48,55]
    Output:[“Fail”,“Pass”,“Pass”,“Fail”,“Pass”]
"""

marks = [35,70,90,48,55]

result = ["P" if m > 50 else "F"  for m in marks]

print(result)