all_numbers = []
number_input = input("Enter a number (or press Enter to quit): ")
while number_input != "":
    number = float(number_input)
    all_numbers.append(number)
    number_input = input("Enter a number (or press Enter to quit): ")
print(f"Smallest number: {min(all_numbers):.1f}\nLargest number: {max(all_numbers):.1f}")

