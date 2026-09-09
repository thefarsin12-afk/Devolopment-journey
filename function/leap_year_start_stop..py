def leap_year(start,stop):

    for i in range(start,stop):
        if (i % 100 ==0 and i % 400 ==0 )or ( i %100!=0 and i %4==0):
         print(i)

leap_year(2000,3000)         