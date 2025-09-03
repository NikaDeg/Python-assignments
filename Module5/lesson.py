# number = int(input("Please enter an integer number: "))
# while number > 0:
#     factorial = 1
#     for i in range (1,number+1):
#         factorial = factorial * i  # factorial *= i
#     print (f"The factorial of the number: {factorial}")
#     number = int(input("Please enter an integer number: "))
#
# print("Thanks and bye")

def spruce_coming(height):
    print("A spruce is coming!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print (" " * empty + "*" * stars )
        i += 1
    print (" " * (height - 1) + "*")

spruce_coming(15)