#!/usr/bin/env python

from brain_games import cli
from brain_games.games import calc_game


def main():
    user_name = cli.welcome_user()
    calc_game.play_game(user_name)


if __name__ == '__main__':
    main()
