"""
Input:  "abcdef"
Output: -1
"""

def first_reqrusive_chara(word):

    lst = []

    for chara in word:

        if chara not in lst:
            lst.append(chara)

        else:
         print(chara)
         return

    print(-1)         

first_reqrusive_chara("abcdef")        