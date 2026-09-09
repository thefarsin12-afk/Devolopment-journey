def merge_str(word1,word2):

    result = ""

    for i in range (0,len(word1)):

        result +=word1[i] + word2[i]

    print(result)

merge_str("PQSR","ABCR")        