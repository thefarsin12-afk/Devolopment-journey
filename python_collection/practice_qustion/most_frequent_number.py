"""
q4)write a program to print most frequent  number
     arr=[10,1,15,16,11,10,12,11,12,18,12]
    o/p => 12
"""

"""array = [10,1,15,16,11,10,12,11,12,18,12]"""

"""most_frequent_number = array[0]

highest_count = 0 

for num in array:

    current_count = array.count(num)

    if current_count > highest_count:

        highest_count = current_count

        most_frequent_number = num

print(most_frequent_number)      """

"""
set most_frequnt number as = 0

repeat for each num in array

chk if frequnacy_of_current_num > frequncy_of_most_frequent number then 
   update mostfrequent number 

display most frequent number    
"""

"""array = [10,1,15,16,11,10,12,11,12,18,12,1,1]

most_frequnt_number = array[0]

for num in array:

    if array.count(num) > array.count(most_frequnt_number):

     most_frequnt_number = num

print(most_frequnt_number)     """

array = [10,11,12,13,10,12,1]

most_frequent = array[0]

for num in array:

    if array.count(num) > array.count(most_frequent):

        most_frequent = num

print(most_frequent)        