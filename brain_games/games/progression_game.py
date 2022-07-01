from random import randint
from brain_games import game_process


def get_game_data():
    progression_length = randint(5, 10)
    hiden_position = randint(1, progression_length) - 1
    start_number = randint(1, 20)
    increment = randint(2, 5)
    progression = []
    number = start_number
    for index in range(progression_length):
        if index == hiden_position:
            progression.append('..')
            hiden_number = number
        else:
            progression.append(str(number))
        if index < (progression_length - 1):
            number += increment
    question = ' '.join(progression)
    correct_answer = str(hiden_number)
    answer_pattern = r'^(\-)?[0-9]+$'
    return question, correct_answer, answer_pattern


def start_game(user_name: str):
    rule_text = 'What number is missing in the progression?'
    game_process.play_game(user_name, rule_text, get_game_data)
