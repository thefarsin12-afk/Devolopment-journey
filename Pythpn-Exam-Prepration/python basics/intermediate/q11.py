"""
Q2

word = "abcdefca"
Find the first repeating character.

Expected:
a
"""

word = "abcdefca"

lst = []

for chara in word:

    if chara not in lst:

        lst.append(chara)

else:
    print(chara)
        
        