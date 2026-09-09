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