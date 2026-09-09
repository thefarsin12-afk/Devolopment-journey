#Same number in each row

# 5 r and 5 c

def same_number():

    for r in range(1,6):

        for c in range(1,r+1):

            print(r, end =" ")

        print()

same_number()            