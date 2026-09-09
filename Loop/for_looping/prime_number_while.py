number = int(input("Enter a number..."))

prime =True

for i in range(2,number):

    if number%i==0:

        prime=False
       
        break

print(prime)