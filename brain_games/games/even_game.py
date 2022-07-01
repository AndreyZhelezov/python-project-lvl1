from random import randint
from brain_games import game_process


def get_game_data():
    random = randint(1, 100)
    question = str(random)
    correct_answer = 'yes' if (random % 2) == 0 else 'no'
    answer_pattern = r'^yes$|^no$'
    return question, correct_answer, answer_pattern


def start_game(user_name: str):
    rule_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_process.play_game(user_name, rule_text, get_game_data)
