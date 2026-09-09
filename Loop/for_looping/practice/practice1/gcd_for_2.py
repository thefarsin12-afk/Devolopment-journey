#10 to 25

num1 = 15

num2 = 25

if num1 < num2:
    smaller = num1

else:
    smaller = num2

gcd = 1

for i in range (1, smaller + 1):
    
    if num1 %i == 0 and num2 % i ==0:

        gcd=i

print(gcd)        