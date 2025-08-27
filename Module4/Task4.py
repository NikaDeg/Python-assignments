import random
random_int = random.randint(1,10)
guessed_number = int(input("Guess a number (1-10): "))
while random_int != guessed_number:
    if random_int > guessed_number:
        print("Too low")
    if random_int < guessed_number:
        print("Too high")
    guessed_number = int(input("Guess a number (1-10): "))
print("Correct")