class Factorial:

    def solution(self,number):

        result = True

        i = 1

        product = 1

        while i <= number:

            product = product * i

            i = i + 1
        print(f"factorial number {number} = {product}")
        return result

factorial_instant = Factorial()    

print(factorial_instant.solution(5))    