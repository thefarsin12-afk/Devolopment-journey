"""
2. First Non-Repeating Occurrence

word = "aabbcdde"
Find the first non-repeating character.

Expected:
c
"""

word = "aabbcdde"

for chara in word:

    if word.count(chara) == 1:
        print(chara)
        break

else:print(-1)