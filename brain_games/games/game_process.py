import prompt
import re


def play_round(question: str, correct_answer: str, answer_pattern: str):
    """Function processes a game round and return 'True' if round successful
    or return 'False' if round unsuccessful."""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if re.fullmatch(answer_pattern, answer) and answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f'\'{answer}\' is wrong answer ;(. '
            f'Correct answer was \'{correct_answer}\'.'
        )
        return False
