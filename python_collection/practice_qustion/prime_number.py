#print prime numbers
arry = [ 3,7,4,9,10,11,12,13]

prime_number = []

for num in arry:

    for i in range (2,num):

        if num % i ==0:
         break

    else:

        prime_number.append(num)

print(prime_number)            