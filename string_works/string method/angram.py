word1 = "night"

word2 = "thing"

for chara in word2:
    if chara not in word1:
        print("Note anagram")
        
        break

else:
    print("angram")    