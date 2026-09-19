# chk first none repeating chara in leet code. output index value

word = "leetcode"

#step1:each character check in word then create for loop
for chara in word:

    #step2: then check chara count in word and chk == 1
    if word.count(chara) == 1:

        #step3:then display none repeated chara index value then exit
        print(word.find(chara))
        break 

#step5:else no unique character print(-1)
else:print(-1) 
