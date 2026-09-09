#Reverse same number
#5 r and 5 c

def reverse_same_number():

    for r in range(5,0,-1):

        for c in range(1,r+1):

            print(r,end=" ")

        print()    

reverse_same_number()        