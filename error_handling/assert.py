def is_palidrome(word):

    result = True
    
    return result


try:
    assert is_palidrome("dad") == True, "test case 1 failed"

    assert is_palidrome("tan") == False, "test case 2 failed"

    assert is_palidrome("malayalam") == True, "test case 3 failed"

except:

    print("error")

else:

    print("Sucess")        