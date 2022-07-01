import prompt
import re
import sys


def play_game(user_name: str, rule_text: str, get_game_data):
    """Function processes a game"""
    round_won = 0
    round_count = 3
    print(rule_text)
    while round_won <= round_count:
        if round_won == round_count:
            print(f'Congratulations, {user_name}!')
            sys.exit(0)
        question, correct_answer, answer_pattern = get_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if re.fullmatch(answer_pattern, answer) and answer == correct_answer:
            print('Correct!')
            round_won += 1
        else:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {user_name}!')
            sys.exit(0)
