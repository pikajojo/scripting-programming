def temperature_transform(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def two_leap_year(year1, year2):
    if leap_year(year1) or leap_year(year2):
        return True
    else:
        return False


if __name__ == "__main__":
    print(temperature_transform(35))
    print(leap_year(2049))
    print(two_leap_year(2034,2024))