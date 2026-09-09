#year note visibile 100 and divicibile by 4
#note equal !=0 
number=int(input("Enter a year"))
value_identify= number%100!=0 and number%4==0
print(value_identify)
