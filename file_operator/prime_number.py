#print(10 to 100)

prime_number = open("file_operator\\prime_number.txt","w")

for i in range (10,101):

    for n in range(2,i):

        if i % n == 0:
            break


    else:
        prime_number.write(str(n)+"\n")  

print("completed")        