"""
year = int(input("Enter a year:"))
if year % 100 == 0 and year % 400 == 0:
    print(f"{year:.0f} is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year:.0f} is a leap year.")
else:
    print(f"{year:.0f} is not a leap year.")
"""

#improved code

year1 = int(input("Enter a year: "))
if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
    print(f"{year1:.0f} is a leap year.")
else:
    print(f"{year1:.0f} is not a leap year.")
