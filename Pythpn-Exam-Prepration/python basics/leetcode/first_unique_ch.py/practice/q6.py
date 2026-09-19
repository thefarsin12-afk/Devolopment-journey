"""
Input:  "aabb cdd"
Output: "c"
"""

def first_none_reqrusive_character(word):

    for chara in word:

        if chara == " ":
            continue

        if word.count(chara) == 1:
            print(chara)
            break

    else:print(-1)

first_none_reqrusive_character("aabb cdd")        
