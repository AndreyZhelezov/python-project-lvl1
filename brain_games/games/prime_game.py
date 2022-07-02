from random import randint
from brain_games import game_process


def isprime(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

def get_game_data():
    random = randint(1, 500)
    question = str(random)
    correct_answer = 'yes' if isprime(random) else 'no'
    answer_pattern = r'^yes$|^no$'
    return question, correct_answer, answer_pattern


def start_game(user_name: str):
    rule_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_process.play_game(user_name, rule_text, get_game_data)
