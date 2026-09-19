#first requrusive chara

s = "leetcode"

for chara in s:

    if s.count(chara) == 1:
        print(chara)
        break

else:print(-1)    