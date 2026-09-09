"""
3.  Get first character of every word
    Input:[“Python”,“Java”,“Django”,“React”] Output:[“P”,“J”,“D”,“R”]
"""

character = ["Python","Java","Django","React"]

reslut = [ch [0] for ch in character]

print(reslut)

for ch in character:

    reslut.append(ch[0])
        
