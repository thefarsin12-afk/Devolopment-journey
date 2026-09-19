"""
Input:  "python code"
Output: "o"
"""

def first_rqrusive_chara(word):

    lst = []

    for chara in word:

        if chara not in lst:

            lst.append(chara)

        else:
            print(chara)

            return

    print(-1)

first_rqrusive_chara("Pythoncode")            