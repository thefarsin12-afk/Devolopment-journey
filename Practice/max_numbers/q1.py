#Find the maximum of 4 numbers.

def max_num(num1,num2,num3,num4):

    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        print(f"Number one is gretaer{num1}")

    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        print(f"Number Two is greater{num2}")    

    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        print(f"Number Three is greater {num3}")   

    else:
        print(f"Number Four is graeter {num4}")    

max_num(10,20,30,25)        