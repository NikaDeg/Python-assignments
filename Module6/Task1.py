def roll_dice():
    import random
    random_dice = random.randint(1, 6)
    return random_dice


number = roll_dice()
while number < 6:
    print (f"{number}")
    number = roll_dice()
if number == 6:
    print ("6")


