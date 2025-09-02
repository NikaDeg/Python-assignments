def roll_dice(sides):
    import random
    random_dice = random.randint(1, sides)
    return random_dice

user_input = int(input("How many sides of dice do you want: "))
number = roll_dice(user_input)
while number < user_input:
    print (f"{number}")
    number = roll_dice(user_input)
print (f"{user_input}")