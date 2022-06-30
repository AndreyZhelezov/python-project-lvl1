#!/usr/bin/env python

from brain_games import cli
from brain_games import even_game


def main():
    user_name = cli.welcome_user()
    even_game.start_game(user_name)


if __name__ == '__main__':
    main()
