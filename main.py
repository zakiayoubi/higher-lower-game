import art
import random
from game_data import data
import os


print(art.logo)
score = 0
continue_game = True

account_b = random.choice(data)
while continue_game:
    def format_data(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return (f"{account_name}, a {account_description}, from {account_country}")


    def check_answer(guess, a_follower_count, b_follower_count):
        if a_follower_count > b_follower_count:
            return guess == 'a'
        else:
            return guess == 'b'


    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers. Type 'A' or 'B' ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(art.logo)
    if is_correct:
        score += 1
        print(f"You're right! Current socre: {score}")

    else:
        continue_game = False
        print(f"Sorry you're wrong. Final score {score}")