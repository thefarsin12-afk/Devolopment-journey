#list vowels,consonats,special character

text = "hello$world"

vowels = []

consonats = []

special_chara = []

for chara in text:

    if chara.lower() in "aeiou":

        vowels.append(chara)

    elif chara.lower().isalpha():

        consonats.append(chara)

    else:
        special_chara.append(chara)

print(f"vowels {vowels}")                    
print(f"consonats {consonats}")                    
print(f"special chara {special_chara}")                    