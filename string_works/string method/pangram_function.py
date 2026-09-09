
def is_pangram(word1):
 
 alphabet = "abcdefghijklmnopqrstuwxyz"

 for chara in alphabet:
  if chara not in word1.lower():
   print(False)
   break

 else:
  print(True)

is_pangram("The quick brown fox jumps over the lAzy dog")    

  
