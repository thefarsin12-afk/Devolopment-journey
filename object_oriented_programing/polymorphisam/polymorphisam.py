# overloading method note working python
#same method using difrent number note work
class Calculator:

    def add(self,num1,num2):
        print(num1+num2)

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)

calculator_instant = Calculator()
calculator_instant.add(10,20,30,40)                
calculator_instant.add(10,20,30)                