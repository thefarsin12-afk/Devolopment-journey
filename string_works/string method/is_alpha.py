"""
is_alpha ()check to string is alphabet
is_digit ()check to string is digit
is_alnum () check to number is alphanumaric
"""

password = "Password@123"

if password.isalpha():

    print("Password is alphabet")

elif password.isalnum():

    print("Password is alphanumaric")

elif password.isdigit():

    print("Password is digit")

else:
    print("Special character included")        

    