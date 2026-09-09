#10. **Login System**: Verify username and password and display success or failure.

user_name = "Noha_12"

user_password = 8901

name = (input("Enter Your User name"))

if name == user_name:

    password = int(input("Enter Your Password"))

    if password == user_password:

        print("Youre Login Sucessfully")

    else:
       print("Inavalid password")

else:
    print("Invalid Username")        