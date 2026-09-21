"""
Q1

word = "programming"

Find the first repeating character.

Expected:
r
"""

word = "programming"

lst = []

for chara in word:

    if chara not in lst:

        lst.append(chara)
        

    else:
        print(chara)
        break