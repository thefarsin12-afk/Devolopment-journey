"""
Input:  "leetcode"
Output: "l"
"""

def first_none_reqrusive(word):

    for chara in word:

        if word.count(chara) == 1:

            print(chara)
            break

    else:print(-1)   

first_none_reqrusive("leetcode")