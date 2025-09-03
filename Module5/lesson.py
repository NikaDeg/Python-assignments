number = int(input("Please enter an integer number: "))
while number > 0:
    factorial = 1
    for i in range (1,number+1):
        factorial = factorial * i  # factorial *= i
    print (f"The factorial of the number: {factorial}")
    number = int(input("Please enter an integer number: "))

print("Thanks and bye")
