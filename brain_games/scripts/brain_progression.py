#!/usr/bin/env python

from brain_games import cli
from brain_games.games import progression_game


def main():
    user_name = cli.welcome_user()
    progression_game.start_game(user_name)


if __name__ == '__main__':
    main()
