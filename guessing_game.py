import random
import time


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


def get_life_count():
    while True:
        try:
            lives = int(input("Enter how many lives you want: "))
            if lives > 0:
                return lives
            else:
                print("Lives must be a positive integer.")
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
        print(
            f"Congratulations you win! You've guessed the number in {count} attempts.")
        input("Press Enter to exit the game.")
        return True, c_lower, c_upper, count

    elif guess < secret:
        print("Too low! Try again.")
        print("")
        if guess >= c_lower:
            c_lower = guess + 1
    elif guess > secret:
        print("Too high! Try again.")
        print("")
        if guess <= c_upper:
            c_upper = guess - 1
    return False, c_lower, c_upper, count


def computer_turn(secret, c_lower, c_upper, c_count):
    guess = random.randint(c_lower, c_upper)
    c_count += 1
    if guess == secret:
        time.sleep(1)
        print(f"Computer guessed {guess}")
        print(f"Computer wins! In {c_count} attempts.")
        input("Press Enter to exit the game.")
        return True, c_lower, c_upper, c_count

    elif guess < secret:
        time.sleep(1)
        print(f"Computer guessed {guess}")
        print("Too low!")
        print("")
        if guess >= c_lower:
            c_lower = guess + 1
    elif guess > secret:
        time.sleep(1)
        print(f"Computer guessed {guess}")
        print("Too high!")
        print("")
        if guess <= c_upper:
            c_upper = guess - 1
    return False, c_lower, c_upper, c_count


def single_player_creative():
    print("Welcome to the Guessing Game!")
    print("You have selected creative mode, you have unlimited lives.")
    print("First, you decide the range for the game.")

    count = 0

    p_won = False

    # unused but required for funtions
    c_lower = 0
    c_upper = 0

    lower = get_lower()
    upper = get_upper(lower)

    secret = random.randint(lower, upper)

    print("Great! Now let's start the game.")
    print(f"try and guess a number between", lower, "and", upper)

    while True:
        p_won, c_lower, c_upper, count = player_turn(
            secret, c_lower, c_upper, count)
        if p_won == True:
            break


def single_player_comp():
    print("Welcome to the Guessing Game!")
    print("You have selected comp, will be playing against me.")
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
        p_won, c_lower, c_upper, count = player_turn(
            secret, c_lower, c_upper, count)
        if p_won == True:
            break
        c_won, c_lower, c_upper, c_count = computer_turn(
            secret, c_lower, c_upper, c_count)
        if c_won == True:
            break


def single_player_survival():
    print("Welcome to the Guessing Game!")
    print("You have selected survival mode, you have limited lives and a range of 1 - 100.")
    print("You can choose between 3 difficulties or a custom mode:")
    print("1. Easy - 10 lives")
    print("2. Medium - 7 lives")
    print("3. Hard - 5 lives")
    print("4. Custom - Choose your own lives and range")

    while True:
        mode = input("PLease Select '1, 2, 3 or 4' ").strip().lower()

        if mode == "1":
            print("You have selected easy mode, you will have 10 lives.")
            lives = 10
            lower = 1
            upper = 100
            break
        elif mode == "2":
            print("You have selected medium mode, you will have 7 lives.")
            lives = 7
            lower = 1
            upper = 100
            break
        elif mode == "3":
            print("You have selected hard mode, you will have 5 lives.")
            lives = 5
            lower = 1
            upper = 100
            break
        elif mode == "4":
            print(
                "You have selected custom mode, you will be able to choose your own lives and range.")
            print("First, choose the range for the game.")
            lower = get_lower()
            upper = get_upper(lower)
            print("Now choose how many lives you want.")
            lives = get_life_count()
            break
        else:
            print("Please enter a valid option")
            continue

    count = 0

    p_won = False

    # unused but required for funtions
    c_lower = 0
    c_upper = 0

    # lower = get_lower()
    # upper = get_upper(lower)

    # lives = get_life_count()

    secret = random.randint(lower, upper)

    print("Great! Now let's start the game.")
    print(
        f"You have {lives} lives to try and guess a number between", lower, "and", upper)
    print("Good luck!")

    while lives > 0:
        p_won, c_lower, c_upper, count = player_turn(
            secret, c_lower, c_upper, count)
        if p_won == True:
            break
        lives -= 1
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            print(
                f"Sorry, you've run out of lives. The secret number was {secret}.")
            input("Press Enter to exit the game.")
            break


def co_op_comp():
    print("Welcome to the Guessing Game!")
    print("You have selected co-op competitive mode, Player 1 will be playing against Player 2.")
    print("First, you decide the range for the game.")

    count = 0
    c_count = 0

    p1_won = False
    p2_won = False

    lower = get_lower()
    upper = get_upper(lower)

    secret = random.randint(lower, upper)
    c_lower = lower
    c_upper = upper

    print("Great! Now let's start the game.")
    print(f"try and guess a number between", lower, "and", upper)
    print("Player 1 will go first.")

    while True:
        print("Player 1's turn:")
        p1_won, c_lower, c_upper, count = player_turn(
            secret, c_lower, c_upper, count)
        if p1_won == True:
            break
        print("Player 2's turn:")
        p2_won, c_lower, c_upper, c_count = player_turn(
            secret, c_lower, c_upper, c_count)
        if p2_won == True:
            break


def choose_mode():
    print("Choose a game mode:")
    print("1. single player - Casual (unlimited lives)")
    print("2. Single Player - Survival (limitied lives)")
    print("3. Single Player - Competitive (You vs Computer)")
    print("4. Co-Op - Competitive (Player 1 vs Player 2)")
    print("5. quit - Exit the game")
    while True:
        try:
            mode = int(input("Enter Game Mode, '1, 2, 3, 4, 5': "))
            if mode == 1:
                single_player_creative()
                return True
            elif mode == 2:
                single_player_survival()
                break
            elif mode == 3:
                single_player_comp()
                return True
            elif mode == 4:
                co_op_comp()
                return True
            elif mode == 5:
                return False
            else:
                print("Please enter a valid option")
                continue
        except ValueError:
            print("Please enter a valid intiger")


def game():
    playing = True
    while playing:
        keep_playing = choose_mode()
        if keep_playing == False:
            print("Thanks for playing!")
            print("press Enter to exit")
            break
        while True:
            play_again = input(
                "Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing!")
                print("press Enter to exit")
                playing = False
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue


game()
