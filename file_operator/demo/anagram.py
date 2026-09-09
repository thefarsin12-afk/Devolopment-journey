word = ["silent","listen","race","care","trap","night","tight"]

fw = open("file_operator\\anagram.txt","w")

for w1 in word:

    for w2 in word:

      if sorted(w1) == sorted(w2) and (w1) != (w2):
         fw.write(w1+"\n")    
 
print("completed")    