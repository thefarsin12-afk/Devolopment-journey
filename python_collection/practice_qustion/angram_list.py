"""
q1) wirte a program to display anagrams
    words=["silent","listen","act","cat","note","tone","hen","chicken"]
    angarms=["silent","listen","act","cat","note","tone"]
"""

"""words=["silent","listen","act","cat","note","tone","hen","chicken"]

angram = []

for w in words:

    for compare_word in words:

        if w != compare_word and sorted(w) == sorted(compare_word):

            if w not in angram:

                angram.append(w)

print(angram)                


word = ["abs","cda","bca","cad","adc"]

angram = set()

for i in range (0,len(word)):

    for j in range(0,len(word)):

        w1 = word[i]

        w2 = word[j]

    if sorted (w1) == sorted (w2) and w1 != w2:

        angram.add(w1)

        angram.add(w2)    

print(angram)        
"""
words=["silent","listen","act","cat","note","tone","hen","chicken"]
#index     0        1      2     3      4      5     6       7
angram = set()

for i in range (0,(len(words))):

    for j in range(0,len(words)):

      w1 = words[i]

      w2 = words[j]

      if sorted(w1) == sorted(w2) and w1 != w2:

         angram.add(w1)
         angram.add(w2)

print(angram)         