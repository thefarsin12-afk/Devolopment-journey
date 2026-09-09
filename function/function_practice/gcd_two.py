def gcd(num1,num2):

    gcd =1

    for count in range(1,min(num1,num2)+1):

     if num1 % count == 0 and num2 % count ==0:

            gcd = count

    print(gcd)

gcd(18,24)             
gcd(24,48)             