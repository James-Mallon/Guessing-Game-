import random
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between two numbers you will provide.")
count = 1

while True:
    lower = input("Enter the lower number: ")
    try:
        lower = int(lower)
        if lower < 1:
            print("The lower number must be greater than 0.")
            continue
        break 
    except ValueError:
        print("Please enter a valid whole number.")
 

while True:
    upper = input("Enter the upper number: ")
    try:
        upper = int(upper)
        if upper <= lower:
            print(f"The upper number must be greater than the lower number ({lower}).")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number greater than the lower limit.")

secret = random.randrange(lower, upper + 1)

print(f"I have selected a number between {lower} and {upper}. Can you guess it?")

while True:
    player_guess = int(input("Enter your quess: "))

    if player_guess == secret: 
        print (f"You won in {count} guesses!")
        input("Press Key to exit")
        break
    else:
        count += 1
        if int(player_guess) < secret:
            print("Your quess is too low!")
        else:
            print("Your quess is too high!")