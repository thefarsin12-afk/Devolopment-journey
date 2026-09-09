'''
✅ 3. Login System with Password and OTP
Task:
Ask for password.
If password is correct:
Ask for OTP
If OTP is correct → "Login successful"
Else → "Incorrect OTP"
Else → "Incorrect password"
'''

password = 1234
otp = 8483

user_password  = int(input("Enter your Password"))

if user_password == password:

    user_otp = int(input("Enter your otp"))

    if user_otp == otp:
        print("Your login Succefully")

    else:
        print("Inavlid OTP number")

else:
    print("Invalid Pssword")            
    