"""
list intro
"""
expenses = [12000 , 11000 , 15000 , 20000]

expence_id = expenses[2]

print(expence_id)

expenses[0]=15000
print(expenses)
"""
print("using index")
for i in range(0 , 5):

    print (expenses[i])

print("amount print")"""

for amount in expenses:
    print(amount)   

     
#tuple
#tuple method no modify,order based,dupilicate allow

tp = (10,30,30)

print(tp)

print(tp.count(30))

print(tp.index(30))

print(type(tp))    

#set
"""
define st={10,20,30} st=(10,20,30)
no orded
no duplacate
updation  avilabile
methods = add,union,insection,difference,is_superset,is_subset
"""

st = {40,10,20,30,50}

print(st)

"""st1 = (10,20,30,40,60)

print(st1)

add=st1.add(20)
print(add)"""

print("set method")
set_a = {10,20,30,100}

set_b = {10,20,30,100,200}

set_union = set_a.union(set_b)
print("u",set_union)

set_intersection = set_a.intersection(set_b)
print("i",set_intersection)

set_difference = set_a.difference(set_b)
print("d",set_difference)

#is superset 
superset = set_a.issuperset(set_b)
print(superset)


#dictionary
#define {key:value}
#order:
#mutabile:yes
#duplicate:key not allowing
#method:.key,.values

daily_calorie = {"mon":2100,
                 "tue":2200,
                 "wed":2200,
                 "thu":2200,
                 "fri":2200,
                 }

print(daily_calorie)

daily_consumed_cal = daily_calorie["fri"]
print(daily_consumed_cal)

#update calorei mon
up_cal = daily_calorie["mon"]=3000
print(up_cal)

print("all keys")

for k in daily_calorie.keys():
    print(k)

print("values")

for v in daily_calorie.values():
    print(v)

#dictionary items method,add key and values
print("keys and values")
for k,v in daily_calorie.items():
    print(k,v)

#get method,usin key value and out put,no varibie, "none" output
monday_cal = daily_calorie.get("mon")
print(monday_cal)
total = daily_calorie.get("total",0)
print(total)

#sum of total calories

total_cal = 0

for v in daily_calorie.values():

   total_cal = total_cal + v

daily_calorie["total caloreis"]=total_cal

print(daily_calorie)

#method 2

