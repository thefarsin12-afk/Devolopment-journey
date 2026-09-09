word1 = "listen"

word2 = "silent"

for chra in word2:
    if chra not in word1 or word1.count(chra) != word2.count(chra):
        print("Note angram")
        break

else:
    print("angram")    