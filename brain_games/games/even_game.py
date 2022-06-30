import sys
from random import randint
from brain_games.games.game_process import play_round


def play_game(user_name: str):
    round_won = 0
    round_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while round_won <= round_count:
        if round_won == round_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        random = randint(1, 100)
        question = str(random)
        correct_answer = 'yes' if (random % 2) == 0 else 'no'
        answer_pattern = r'^yes$|^no$'
        if play_round(question, correct_answer, answer_pattern):
            round_won += 1
        else:
            sys.exit(0)
