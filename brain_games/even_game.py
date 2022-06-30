import sys

import prompt
from random import randint


def play_game(user_name: str):
    answer_count = 0
    target_answer_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while answer_count <= target_answer_count:
        if answer_count == target_answer_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        random = randint(1, 100)
        correct_answer = 'yes' if (random % 2) == 0 else 'no'
        print(f'Question: {random}')
        answer = prompt.string('Your answer: ')
        if answer in ['yes', 'no'] and answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            sys.exit(0)
