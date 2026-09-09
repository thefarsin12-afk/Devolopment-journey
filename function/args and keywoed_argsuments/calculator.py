# ** caluculaator operatopn seting to key word

def calculator(*args,**kwargs):

    if kwargs.get("operations") == "+":

        return sum(args)

    elif kwargs.get("operations") == "*":

        result = 1

        for num in args:

            result = result * num

        return result    

print(calculator(10,20,30,40,operations="*"))  
    
    