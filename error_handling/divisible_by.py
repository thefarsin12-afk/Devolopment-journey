def is_divisible(num):

    result = True

    if num% 3 ==0:

     result = True

    else:      
      result =False
    return result

assert is_divisible(9)==True, "test case1 failed"
assert is_divisible(16)==False, "test case2 failed"