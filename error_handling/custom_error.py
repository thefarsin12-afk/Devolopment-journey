#custom error "raise"
print("custom error...")

age = int(input("Enter a your age"))

if age < 18:

    raise Exception ("Inavalid age")

else:
    print("Youre eligible for vote")