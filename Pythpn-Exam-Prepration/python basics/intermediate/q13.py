"""
Q4
word = "aabbccdde"

Find the first non-repeating character.

Expected:
e
"""

word = "aabbccdde"

for chara in word:

    if word.count(chara) == 1:
        print(chara)
        break

else:print(-1)