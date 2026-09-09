# set a match case

number = int(input("Enter a number"))

match number:
    case 1:
        print("Appile")

    case 2:

        print("Banana")
    case 3:

        print("Orange")
    case 4:

        print("Stawbery")
    case _:
        
        print("Inavlid number")