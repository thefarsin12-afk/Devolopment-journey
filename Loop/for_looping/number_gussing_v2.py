secret_number=7

for attempt in range(1,10):

    num =int(input("Enter a number...."))

    if num == secret_number:
        print("Congradulation")

    elif num >secret_number:
        print("litile high")
    
    elif num <secret_number:
        print("litile small")

if num>5:
    print("Youre attempt is over")

