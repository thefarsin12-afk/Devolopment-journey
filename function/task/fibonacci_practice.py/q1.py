"""
Print the first n Fibonacci numbers.
Example:
Input: 8
Output: 0 1 1 2 3 5 8 13
"""
def first_number(number):

    first = 0

    second = 1

    count = 0

    while count < number:

      print(first)

      next = first + second
    
      first = second 

      second = next

      count = count + 1

first_number(8)   


     

        
