def kangaroo_word(word1,word2):

    index = 0

    for w in word1:

        if index < len(word2) and w.lower() == word2[index].lower():
            index += 1

    if index == len(word2):
        print("Kangaroo Word")

    else:print("Not Kangaroo Word")            

kangaroo_word(word1="Think",word2="Ink")