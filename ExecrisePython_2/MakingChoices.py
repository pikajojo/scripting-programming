import calendar
class Iterations():
    # we return the boolean because we can use it later if needed. A print is basically useless on its own.
    # Print is more for debugging. but in principle, for debugging, you should use the ... *drum rolls* ... debugger.
    def is_leap_year(self, year):
        if year == 0:
            return False
        if year % 4 != 0:
            return False
        elif year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
        elif year % 400 == 0:
            return True


    #  it is never a good idea to reinvent the wheel. Use the available libraries! It's easy in python! (pip)
    def is_leap_year_2(self, year):
        return calendar.isleap(year)


if __name__=="__main__":
    iterations = Iterations()
    print(iterations.is_leap_year_2(2016))
    print(iterations.is_leap_year(2016))
