s = "hello guys"

for chara in s:

    if s.count(chara) == 1:

        print(s.find(chara))
        break

else:print(-1)    