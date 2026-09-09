#checking pangram
text =  "The quick brown fox jumps over the lazy dog"

alpha_bets="abcdefghijklmnopqrstuwxyz"

for chara in alpha_bets:

    if chara not in text:
        print("Not pangram text")
        break

else:
    print("Pangram text")        