
"""w.a.p to display alphabet_count , digit_count """

text="england won by 6 wickes with 3 balls remaining. england leads the series with 2-1"

alphabet_count = 0

digit_count = 0

for check in text:

    if check.isalpha():

        alphabet_count += 1

    elif check.isdigit():

        digit_count += 1

print(f"alphabet_count,{alphabet_count} ")        
print(f"digit_count,{digit_count} ")        

