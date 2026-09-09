fw = open("file_operator\\intro\prime_number.txt","w")

for i in range (50,100):

 for num in  range(2,i):
      if num % i == 0:
        break
else:
    fw.write(str(num)+"\n") 

print("complted")

    