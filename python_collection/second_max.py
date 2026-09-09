#second max identify without max and min

placement = [10,15,22,9,17,18]

first_max,secocond_max =0,0

for count in placement:

    if count > first_max:

        secocond_max = first_max

        first_max = count

    elif count > secocond_max:

        secocond_max = count

print(secocond_max)            