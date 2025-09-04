# def get_season(month_number):
#     if month_number == 1 or month_number == 2 or month_number == 12:
#         season = "winter"
#     elif month_number == 3 or month_number == 4 or month_number == 5:
#         season = "spring"
#     elif month_number == 6 or month_number == 7 or month_number == 8 :
#         season = "summer"
#     else:
#         season = "autumn"
#     return season
#
# month = int(input("Enter the number of a month (1-12): "))
# if 1 <= month <= 12:
#     print(f"You entered: {month}")
#     season = get_season(month)
#     print(f"The season is {season}.")
# else:
#     print(f"You entered: {month}")
#     print("Please enter a number between 1 and 12.")

def get_season(month):
    seasons_order = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
    season = seasons_order[month-1]
    print(f"You entered: {month}\nThe season is {season}.")

month = int(input("Enter the number of a month (1-12): "))
if 1 <= month <= 12:
    get_season(month)
else:
    print(f"You entered: {month}")
    print("Please enter a number between 1 and 12.")