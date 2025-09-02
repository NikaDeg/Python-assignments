rolls = int(input("How many dice to roll: "))
import random
sum = 0
for _ in range(rolls):
    dice = random.randint(1,6)
    sum = sum + dice
print (f"Sum of the dice: {sum}")