class Leap_year:

    def solution(self,year):

        result = True

        if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
         print(f"leap year {year}")
         return result

leap_year_instant = Leap_year()
print(leap_year_instant.solution(2024))    