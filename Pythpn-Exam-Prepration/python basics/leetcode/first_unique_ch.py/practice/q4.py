"""
Input:  "leetcode"
Output: 0 ..index
"""

def first_none_reqrusive_chara(word):

    for chara in word:

        if word.count(chara) == 1:
            print(word.find(chara))
            break

    else:
        print(-1)

first_none_reqrusive_chara("leetcode")            