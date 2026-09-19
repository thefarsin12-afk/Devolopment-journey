"""
Input: "swiss"
Output: "s"
"""

def friquernt_chara(word):

    lst = []

    for chara in word:

        if chara not in lst:

            lst.append(chara)

        else:
            print(chara)

            return

    print(-1)

friquernt_chara("swiss")            