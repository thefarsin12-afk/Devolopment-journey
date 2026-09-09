from random import randint

secret_number = randint(1,10)

for i in range(1,6):

    number= int(input("Enter a number...."))

    if number == secret_number:

        print("You find it 👍")

        break

if i>= 5:

    print("its over")

