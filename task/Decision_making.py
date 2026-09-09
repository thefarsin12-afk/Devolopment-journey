"""
Write a program to check whether a number is:
Positive
Negative
Zero
"""

def positive_negative_zero(number):

    if number >0:
        print("Postive")

    elif number <0:
        print("Negative")

    else:print("Zero")

positive_negative_zero(-10)            

"""
2. Eligible to Vote
Write a program to check whether a person is eligible to vote.
Condition:
Age >= 18 → Eligible
Otherwise → Not Eligible
"""

print("Vote Eligibility")
age = 18
adhar_card = "yes"
def voting_eligibilty(age,adhar_card):


    if age >= 18 and adhar_card.lower() == "yes":
        print("Youre eligible for vote")

    else:print("Yure not eligible")    

voting_eligibilty(20,"yes")    

"""
3. Largest of Two Numbers
Write a program to find the larger of two numbers.
"""
print("Find largest number")

def largest_number(num1,num2):

    if num1 > num2:
        print(f"largest number is {num1}")

    else:print(f"largest number is {num2}")  

largest_number(10,25)      

"""
Divisible by 5 and 11
Write a program to check whether a number is divisible by both 5 and 11.
"""

def divisible_number (num1):

    if num1 % 5 == 0 and num1 % 11 ==0:
        print("Divisible by both and 11")

    else:print("Not divisible")    

divisible_number(5)    

"""
5. Pass or Fail
Write a program to check whether a student has passed.
Condition:
Marks >= 35 → Pass
Otherwise → Fail
"""

mark = 35

def exam_mark(mark):

 if mark >= 35:
     print("Passed")

 else:print("Failed")

exam_mark(40)

"""
6. Even or Odd
Write a program to check whether a number is even or odd.
"""

def even_or_odd(number):

    if number % 2 ==0:
        print("Even number")

    else:print("Number is odd")

even_or_odd(7)        

"""
1. Largest of Three Numbers
Write a function to find the largest among three numbers.
"""

def largest(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
        print("Number 1 is larger")

    elif num2 >= num1 and num2 >= num3:
        print("Number 2 is greater")

    else:print("Number 3 is greater")

largest(30,30,10)    

"""
2. Leap Year Checker
Write a program to check whether a year is a leap year.
"""

def leap_year(year):

    if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 ==0:
        print("Leap Year")

    else:print("Not leap year") 

leap_year(2021)       

"""
3. Grade Calculator
Write a program to display the grade based on marks.
Marks	Grade
90–100	A
80–89	B
70–79	C
60–69	D
35–59	E
Below 35	F
Also check if the marks are invalid (less than 0 or greater than 100)
"""

def grade_based_mark(mark):

    if mark >= 90:
        print("A")

    elif mark >= 80 and mark <= 89:
        print("B")    

    elif mark >= 70 and mark <=79:
        print("C")

    elif mark >= 60 and mark <= 69:
        print("D")        

    elif mark >= 35 and mark <= 59:
        print("E")

    else:print("F")

grade_based_mark(120)           

"""
4. Electricity Bill Calculator

Calculate the electricity bill based on the units consumed.
Units	Rate per Unit

First 100 units	₹5
Next 100 units	₹7
Above 200 units	₹10
"""
bill = 0

def electricity_bill_cal(unit):

    if unit <= 100:

        bill = unit * 5
        

    elif unit <= 200:
        bill = (100 * 5) + ((unit - 100 )* 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((unit - 200) *10)

    print(bill)

electricity_bill_cal(80)        
electricity_bill_cal(150)        
electricity_bill_cal(250)       


"""
5. ATM Withdrawal
Write a program to check whether a withdrawal is successful.
Conditions:
Balance must be enough.
Withdrawal amount must be a multiple of 100.
Minimum balance after withdrawal must be ₹500.
"""

balance = 100000

atm_pin = 1234

pin = int(input("Enter your pin number..."))

if pin == atm_pin:

    withdrw = int(input("Collect your cash..."))

    if withdrw <= balance:

        print("Withdrw is sucsessfully")

    else:print("Invalid attempt")    

else:print("Invalid attempt")    
    