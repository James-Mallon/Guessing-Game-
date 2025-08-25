import random
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between two numbers you will provide.")

lower = int(input("Enter the lower number: "))
while lower < 1: 
    print("The lower number must be greater than 0.")
    lower = int(input("Please enter a number greater than 0: "))

upper = int(input("Enter the upper number: "))
while upper <= lower: 
    print("The upper number must be greater than the lower number.")
    upper = int(input(f"Please enter a number greater than {lower}: "))

secret= random.randrange(lower, upper + 1)

print(f"I have selected a number between {lower} and {upper}. Can you guess it?")

while True:
    player_guess = int(input("Enter your quess: "))

    if player_guess == secret: 
        print ("You win!")
        input("Press Key to exit")
        break
    else:
        if int(player_guess) < secret:
            print("Your quess is too low!")
        else:
            print("Your quess is too high!")