"""number = int(input("Enter a number"))

gcd=1

for i in range(1,number):
    if number % i==0:
        gcd=i

print(gcd)  
    """

def last_divisor(number):
    gcd=1
    for i in range(1,number):
     
     if number%i==0:
      
      gcd=i

    print(gcd)

last_divisor(8)        