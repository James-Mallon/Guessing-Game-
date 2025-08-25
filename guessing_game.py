import random
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

secret= random.randrange(lower, upper + 1)


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