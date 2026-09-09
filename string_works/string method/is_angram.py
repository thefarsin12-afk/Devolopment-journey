def is_anagram (word1,word2):

    word1 = word1.lower()
    word2 = word2.lower()

    for chara in word1:
        if chara not in word2 or word1.count(chara) != word2.count(chara):
            print(False)
            break
            

    else:
        print(True)

is_anagram("listen","silenT")            