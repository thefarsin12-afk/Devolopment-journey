def palindrome_count (start,end):

    count = 0

    while start <= end:

     orginal = start

     number = start

     revers = 0

     while number != 0:

        last_dgit = number % 10

        revers = revers * 10 + last_dgit

        number = number // 10

     if orginal == revers:
       count += 1

     start += 1

    print(count)

palindrome_count(10, 30)       