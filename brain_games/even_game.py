import sys

import prompt
from random import randint


def start_game(user_name: str):
    correct_count = 0
    target_correct_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_count <= target_correct_count:
        if correct_count == target_correct_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        random = randint(1, 100)
        correct_answer = 'yes' if (random % 2) == 0 else 'no'
        print(f'Question: {random}')
        answer = prompt.string('Your answer: ')
        if answer not in ['yes', 'no'] or answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            correct_count = 0
        else:
            print('Correct!')
            correct_count += 1
