import sys
from brain_games.games.game_process import play_round
from math import gcd, sqrt
from random import randint


def get_gcd_data(top_limit=200):
    """Function return two numbers which gcd is very likely over '1'"""
    base_number = randint(1, int(sqrt(top_limit)))
    first_multiplier = randint(1, int(sqrt(top_limit)))
    second_multiplier = randint(1, int(sqrt(top_limit)))
    first_number = base_number * first_multiplier
    second_number = base_number * second_multiplier
    return first_number, second_number


def play_game(user_name: str):
    round_won = 0
    round_count = 3
    print('Find the greatest common divisor of given numbers.')
    while round_won <= round_count:
        if round_won == round_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        first_number, second_number = get_gcd_data()
        question = f'{first_number} {second_number}'
        correct_answer = str(gcd(first_number, second_number))
        answer_pattern = r'^[0-9]+$'
        if play_round(question, correct_answer, answer_pattern):
            round_won += 1
        else:
            print(f'Let\'s try again, {user_name}!')
            sys.exit(0)
