import prompt


def welcome_user():
    """Function welcomes user and return his or her name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
