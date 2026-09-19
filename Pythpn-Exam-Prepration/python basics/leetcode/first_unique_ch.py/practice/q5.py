"""
Find the first non-repeating character ignoring spaces.

Input:  "aabb cdd"
Output: " "
"""

def first_none_reqrusive_chara(word):

    for chara in word:

        if word.count(chara) == 1:
            print(chara)
            break

    else:
        print(-1)

first_none_reqrusive_chara("aabb cdd")            