"""
print("what a good coffee this morning")
print('"Hello", said Joe')
#escaping symbols
print("\"Hello\", said Joe")
print('I\'m Nika')
print("New\nLine")

from operator import truediv

#new task
name = input("Give name: ")
#print(name)
#print("user = " + name + "!")
print("Nice to meet you, " + name + "!")

#types
string = "string, any text "
numbers = 123
number = 1
print(numbers + number)
print(string + str(number)) #by adding str() we can change number type to string type and print in one string
#int() or float() is converting e.g. string to number

boolean = True
boolean2 = False
"""

# # talents = float(input("Enter talents: "))
# talents = 2.5
# # pounds = float(input("Enter pounds: "))
# pounds = 3.75
# # lots = float(input("Enter lots: "))
# lots = 8.25
# # total_grams = ((talents * 20.0 + pounds) * 32.0 + lots) * 13.3
# total_grams = talents*20*32*13.3 + pounds*32*13.3 + lots*13.3
# print(total_grams)
# kilograms = int(total_grams / 1000)
# print(kilograms)
# remaining_grams = total_grams - (kilograms * 1000)
# print(remaining_grams)
# print("The weight in modern units:")
# print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
#
# 22985.725000000002
# 22985.725

import random
range1 = random.randint(0,9)
range2 = random.randint(1,6)
three_digit_code = (range1, range1, range1)
# print(f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
print(f"{range1}{range1}{range1}")
#four_digit_code = (range2 range2 range2 range2)
#print (f"3-digit code: {three_digit_code} \n4-digit code: {four_digit_code}")