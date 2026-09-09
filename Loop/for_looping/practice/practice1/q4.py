#Print all leap years from 1800 to 2027.

for i in range(1800,2028):
    
    if (i % 100 == 0 and i % 400 == 0) or (i % 100 !=0 and i % 4 == 0):
      
      print(i)