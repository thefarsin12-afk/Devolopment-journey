#palidrome write
word = ["madam","man","chicken"]
fw = open("file_operator\\palindrome.txt","w")

for w in word:

    if w == w[::-1]:
    
      fw.write(w)

print("completed")