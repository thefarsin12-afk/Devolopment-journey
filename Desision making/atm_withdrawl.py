'''
Task:
Ask for PIN.
If PIN is correct
Ask for withdrawal amount
If amount ≤ balance → "Withdrawal successful"
Else → "Insufficient balance"
Else → "Incorrect PIN"
'''

data_pin = 1234

data_bal = 50000

atm_pin=int(input("Enter PIN"))
 
if atm_pin==data_pin:
    amount=int(input("Enter your amount"))
    if amount==data_bal:
     print("Withdraw Succefully")

    else:
       print("amount is inavlid")

else:
   print("Inavlid pIN number")       




  
