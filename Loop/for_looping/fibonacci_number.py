first = 0

second = 1

num = int(input("Enter number"))

for i in range(num):
    print(first)

    next = first+second
    first =second
    second=next

