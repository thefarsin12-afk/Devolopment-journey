"""
Input:  "programming"
Output: "r"
"""

def first_reqrusive_chara(word):

    lst = []

    for chara in word:

        if chara not in lst:

            lst.append(chara)

        else:
         print(chara)
         break

first_reqrusive_chara("programming")        