def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters

users_gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
while users_gallons >= 0:
    converted = gallons_to_liters(users_gallons)
    print(f"{users_gallons:.1f} American gallons is {converted:.2f} liters.")
    users_gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
print("Program finished.")