# identify first repeated character

word = "hello world"

# step:1 create emplty list
lst = []

# step:2 each character check in word so create for loop
for chara in word:

# then check chara not in word
    if chara not in lst:

#then add to lst
      lst.append(chara) 

#chara in lst

    else:
       print(chara)
       break         



