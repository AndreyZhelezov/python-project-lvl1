import sys
from random import randint, choice
from brain_games.games.game_process import play_round


def play_game(user_name: str):
    round_won = 0
    round_count = 3
    print('What is the result of the expression?')
    while round_won <= round_count:
        if round_won == round_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        first_number = str(randint(1, 100))
        second_number = str(randint(1, 100))
        operator = choice(['+', '-', '*'])
        question = f'{first_number} {operator} {second_number}'
        correct_answer = str(eval(question))
        answer_pattern = r'^(\-)?[0-9]+$'
        if play_round(question, correct_answer, answer_pattern):
            round_won += 1
        else:
            print(f'Let\'s try again, {user_name}!')
            sys.exit(0)
