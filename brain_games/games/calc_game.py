from random import randint, choice
from brain_games import game_process


def get_game_data():
    first_number = str(randint(1, 100))
    second_number = str(randint(1, 100))
    operator = choice(['+', '-', '*'])
    question = f'{first_number} {operator} {second_number}'
    correct_answer = str(eval(question))
    answer_pattern = r'^(\-)?[0-9]+$'
    return question, correct_answer, answer_pattern


def start_game(user_name: str):
    rule_text = 'What is the result of the expression?'
    game_process.play_game(user_name, rule_text, get_game_data)
