from game_data import data
from art import logo, vs
import random

print(logo)
score = 0
game_on = True

# format data
# 'name': 'Ariana Grande',
# 'follower_count': 183,
# 'description': 'Musician and actress',
# 'country': 'United States'

def format(account):
    """ Format the account data into printable format """
    acc_name = account['name']
    acc_count = account['follower_count']
    acc_desc = account['description']
    acc_country = account['country']
    return f'{acc_name}, a {acc_desc}, from {acc_country}'

def check_answer(guess, a_followers, b_followers):
    """
    takes the user guess and checks if they are right
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


account_b = random.choice(data)
while game_on:
    # generate 2 random accounts
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}.")
    print(vs)
    print(f"Against: {format(account_b)}.")

    #ask user for a guess
    guess = input("who has more followers 'A' or 'B' : ").lower()

    # check if the answer is correct
    # score keeping
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print("that is correct!!")
    else:
        print(f"sorry that is not correct, your score is {score}")
        game_on = False