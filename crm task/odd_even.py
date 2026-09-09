class Odd_Even:

    def solution(self,number):

        result = True

        if number % 2 == 0:
           print("Even Number")
           return False
   
        else:
           print("Odd number")
           return result


odd_even_instant = Odd_Even()

print(odd_even_instant.solution(2))