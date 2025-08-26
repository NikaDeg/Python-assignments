year = float(input("Enter a year: "))
if year % 100 == 0 and year % 400 == 0:
    print(f"{year:.0f} is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year:.0f} is a leap year.")
else:
    print(f"{year:.0f} is not a leap year.")




'''
just my first attempt without knowing the function %, I left it for memory :)

year = float(input("Enter a year: "))
result_of_division = year / 4
division_by_hundred = year / 100
division_by_fourhundred = year / 400
if division_by_hundred == int(division_by_hundred) and division_by_fourhundred == int(division_by_fourhundred):
    print(f"{year:.0f} is a leap year.")
elif result_of_division == int(result_of_division) and division_by_hundred != int(division_by_hundred):
    print(f"{year:.0f} is a leap year.")
else:
    print(f"{year:.0f} is not a leap year.")
'''