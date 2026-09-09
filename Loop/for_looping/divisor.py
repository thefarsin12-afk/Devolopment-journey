# write a divisor note one and common number/primee number program

num = int(input("Enter a number"))

for i in range(2,num):

    if num % i ==0:
      
      print("note a prime number")
      break

else:
    print("no divisor exit")        