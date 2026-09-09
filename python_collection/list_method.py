#append
#store to end of the list
colors =  ["red" , "green" , "blue", "violet", "purpule" ]
colors.append("white")
print(colors)

#insert
#index,object based on index value
colors.insert(2,"Black")
print(colors)

#remove list method
#pop ,index based remove
# no value auto -1
colors1 =  ["red" , "green" , "blue", "violet", "purpule" ]
#             0        1         2       3          4
colors1.pop(2)
print(colors1)

#remove,removing to value and based first occurence
colors2 =  ["red" , "green" , "blue", "violet", "purpule" ]
colors2.remove("green")
print(colors2)

#index value indentify 
colors3 =  ["red" , "green" , "blue", "violet", "purpule" ]
blue_color = colors3.index("blue")
print(blue_color)

#count : value frequncy count
colors4 =  ["red" , "green" , "blue", "violet", "purpule" ]
count_green = colors4.count("green")
print(count_green)

#reverse
colors5 =  ["red" , "green" , "blue", "violet", "purpule" ]
colors5.reverse()
print(colors5)

#sort(), asending sort(),decending,reverse = True
colors6 =  ["red" , "green" , "blue", "violet", "purpule" ]
colors6.sort(reverse=True)
print(colors6)

#copy
farsin_fvt_food = ["egg","chicken","tea"]
ayush_fvt_food = farsin_fvt_food.copy()
ayush_fvt_food[0]="fried rice"
print(farsin_fvt_food)
print(ayush_fvt_food)