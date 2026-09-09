def leap_year(year):

    if year %100==0 and year % 400==0 or year % 100 !=0 and year % 4==0:
        print(True)

    else:
        print(False)

leap_year(2025)                