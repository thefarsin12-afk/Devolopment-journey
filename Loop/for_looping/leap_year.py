# leap year 1800 to 2027

for year in range(1800,2028):
    
    if year % 100 ==0 and year % 400 ==0 or year % 100 !=00 and year % 4 ==0:
      print(year)
 