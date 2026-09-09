"""
create a file placementcountcasestudy.py
store last 6 month placementcounts as 10,15,22,9,17,18
q) display feb month placementcount 
q) update jan month placementcount as 12
q) display placementcounts where count > 15
q) display highestplacementcount without using max()
q) display lowestplacementcount without using min()
q) display secondhighestplacement_count without using sorted()
"""

placement = [10,15,22,9,17,18]

print("Februvary Placement Count")
feb_placement_count = placement [1]
print(feb_placement_count)

print("Januvary Placement Count Updation")
update_januvary_month_count = placement[0] = 12
print(update_januvary_month_count)

print("Placement greterthan 15")
for count in placement:

    if count > 15:
        print(count)

print("Highest ,Smallest , Second Highest")

highest = placement[0]

smallest = placement[0]

second_highest = placement[0]

for count in placement:

#highest_chk   
    if count > highest:
      highest = count

#smallest_chk       
    if count < smallest:
     smallest = count

#second_highest_chk
    if count > second_highest and count != highest:
      second_highest = count
    
print(f"Highest Placement Count={highest}") 
print(f"Smallest Placement Count={smallest}")
print(f"Second Highest={second_highest}")
#summaraze qystions





