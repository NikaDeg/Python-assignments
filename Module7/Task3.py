airports = {}

option = int(input(
    "\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))

while option != 3:
    if option == 1:
        code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        print(f"Airport {name} with ICAO code {code} has been added.")
        airports[code] = name
    elif option == 2:
        code = input("Enter the ICAO code: ")
        if code in airports:
            print(f"The airport with ICAO code {code} is {airports[code]}.")
        else:
            print(f"No airport found with ICAO code {code}.")
    option = int(input(
        "\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))
print("Thank you for using the Airport Data Management system. Goodbye!")

# EFHK
# Helsinki-Vantaa Airport