import random 

def get_lower():
    while True:
        try:
            lower = int(input("Enter the lower bound: "))
            if lower > 0:
                return lower
            else:
                print("Lower bound must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        
def get_upper(lower):  
    while True:
        try:
            upper = int(input("Enter the upper bound: "))
            if upper > lower:
                return upper
            else:
                print("Upper bound must be greater than lower bound.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def player_turn(secret, c_lower, c_upper, count):
    while True:
        try:
            guess = int(input("Guess a number: "))
            count += 1
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if guess == secret:
        print(f"Congratulations you win! You've guessed the number in {count} attempts.")
        input("Press Enter to exit the game.")
        return True, c_lower, c_upper, count

    elif guess < secret:
        print("Too low! Try again.")
        if guess >= c_lower:
            c_lower = guess + 1
    elif guess > secret:
        print("Too high! Try again.")
        if guess <= c_upper:
            c_upper = guess - 1
    return False, c_lower, c_upper, count

def computer_turn(secret, c_lower, c_upper, c_count):
    guess = random.randint(c_lower, c_upper)
    c_count += 1
    if guess == secret:
        print(f"Computer guessed {guess}")
        print(f"Computer wins! In {c_count} attempts.")
        input("Press Enter to exit the game.")
        return True, c_lower, c_upper, c_count
    elif guess < secret:
        print(f"Computer guessed {guess}")
        print("Too low!")
        if guess >= c_lower:
            c_lower = guess + 1
    elif guess > secret:
        print(f"Computer guessed {guess}")
        print("Too high!")
        if guess <= c_upper:
            c_upper = guess - 1
    return False, c_lower, c_upper, c_count

        

def game():
    print("Welcome to the Guessing Game!")
    print("You will be playing against me.")
    print("First, you decide the range for the game.")

    count = 0
    c_count = 0
    
    p_won = False
    c_won = False
    
    lower = get_lower()
    upper = get_upper(lower)

    secret = random.randint(lower, upper)
    c_lower = lower
    c_upper = upper

    print("Great! Now let's start the game.")
    print(f"try and guess a number between", lower, "and", upper)

    while True:
        p_won, c_lower, c_upper, count = player_turn(secret, c_lower, c_upper, count)
        if p_won ==  True:
            break
        c_won, c_lower, c_upper, c_count = computer_turn(secret, c_lower, c_upper, c_count)
        if c_won == True:
            break

game()
