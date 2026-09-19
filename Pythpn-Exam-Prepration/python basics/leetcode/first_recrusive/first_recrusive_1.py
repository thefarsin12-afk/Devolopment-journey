word = "muhammed farsin"

lst = []

for chara in word:

    if chara not in lst:

        lst.append(chara)

    else:
        print(f"first requresive chara = {chara}") 
        break   