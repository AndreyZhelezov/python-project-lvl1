from math import sqrt, gcd
from random import randint
from brain_games import game_process


def get_gcd_numbers(top_limit=200):
    """Function return two numbers which GCD
    is highly likely is grater then '1'"""
    base_number = randint(1, int(sqrt(top_limit)))
    first_multiplier = randint(1, int(sqrt(top_limit)))
    second_multiplier = randint(1, int(sqrt(top_limit)))
    first_number = base_number * first_multiplier
    second_number = base_number * second_multiplier
    return first_number, second_number


def get_game_data():
    first_number, second_number = get_gcd_numbers()
    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    answer_pattern = r'^[0-9]+$'
    return question, correct_answer, answer_pattern


def start_game(user_name: str):
    rule_text = 'Find the greatest common divisor of given numbers.'
    game_process.play_game(user_name, rule_text, get_game_data)
