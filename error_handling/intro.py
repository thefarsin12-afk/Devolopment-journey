"""
Error_handling

   type of errors
     1.logical error
     2.syntax error
     3.runtime error (try,exepcpt,finally ==>:  raise,assert==>key)

     try = doubtful code ":"
     exepct = exepctation writing ":"
     finally = clean up processing ":"

     raise = creating custom error "key"
     assert = dubugging
     
"""

num1 = int(input("Enter a number..."))

num2 = int(input("Enter a number..."))

try:
    result = num1 / num2

    print("result",result)

except Exception as e:

    print(e)    

print("db transcation...")

print("file writing")