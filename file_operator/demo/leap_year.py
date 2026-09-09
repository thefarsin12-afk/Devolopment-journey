#1800 to 2026

fw = open("file_operator\\intro\leep_year.txt","w")

for i in range (1800 ,2026):

    if i % 100 == 0 and i % 400 == 0 or  i % 100 !=0 and i % 4 ==0:

        fw.write(str(i)+"\n")
        
print("complted")