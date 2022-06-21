from art import logo, vs
from game_data import data
import random
from sty import fg, bg ,ef, rs
import os
clear = lambda: os.system('cls')
clear()

# Definitions
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the users guess and follower counts and returns if they got it right. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make game repeatable
while game_should_continue:

    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # Ask user for a guess.
    breakline = fg.yellow + '-----------------------------------------------------------------' + fg.rs
    print(breakline)
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()


    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear screen between rounds.
    clear()
    print(logo)

    # Feedback.
    if is_correct:
        score += 1
        greenline = fg.green + '===============================' + fg.rs
        print(greenline)
        print(f"You're right! Current score: {score}")
        print(greenline)
        print()
    else:
        redline = fg.red + '=================================================' + fg.rs
        print(redline)
        print(f"Sorry, you got it wrong! Your final score is: {score}")
        print(redline)
        game_should_continue = False

    