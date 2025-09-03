def calculate_unit_price(cm, price):
    r_in_meters = cm / 200
    unit_price = price / r_in_meters ** 2 / 3.1416
    return unit_price


first_d = float(input("Enter the diameter of the first pizza (cm): "))
first_price = float(input("Enter the price of the first pizza (euros): "))
second_d = float(input("Enter the diameter of the second pizza (cm): "))
second_price = float(input("Enter the price of the second pizza (euros): "))
first_unit_price = calculate_unit_price(first_d, first_price)
second_unit_price = calculate_unit_price(second_d, second_price)
print(f"Unit price of the first pizza: {first_unit_price:.2f} euros/m²")
print(f"Unit price of the second pizza: {second_unit_price:.2f} euros/m²")
if first_unit_price < second_unit_price:
    print("The first pizza provides better value for money.")
else:
    print("The first pizza provides better value for money.")