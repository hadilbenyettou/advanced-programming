year = int(input("Please type in a year : "))


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if leap_year(year):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
