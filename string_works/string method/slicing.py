#extract a sequnce in portion
text = "a grammatical unit of one or m"
     #  012345678901234567890123456789
     #            1         2

substr = text[0:13]
print(substr)

substr1 =text[14:18]
print(substr1)

text1 = "extract plan"
        #012345678901
         #         1

substr3 = text1[8:]    
print(substr3)

text4 ="extract panama"
    #   01234567890123
    #             1

substr4 = text4[8:]
print(substr4)    

text ="A Man is perfect human"
    #  0123456789012345678901

substr_man = text[:5]
print(substr_man)

text_copy = text[:]
print(text_copy)

# step parameter
#::2 start,stop,step
step_text = "carracer"

str_text = step_text [::2]

print(str_text)


wtep_text1 = "warracer"

wtr_text = step_text [::3]

print(wtr_text)

#reverse method

reverse_text1 = "racecar1"

reverse_str = reverse_text1[::-1]

print(reverse_str)

