"""
Input:  "aabbcc"
Output: -1
"""

def first_reqrusive_chara(word):

    for chara in word:

        if word.count(chara) == 1:
            print(chara)
            break

    else:
        print(-1)

first_reqrusive_chara("aabbcc")            