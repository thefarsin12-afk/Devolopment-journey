class Gcd:

    def solution(self,number1,number2):

        result = True

        while number2 != 0:

            rem = number1 % number2

            number1 = number2

            number2 = rem

        print(f"GCD = {number1}")    
        return result

gcd_instant = Gcd()

print(gcd_instant.solution(7,5))

