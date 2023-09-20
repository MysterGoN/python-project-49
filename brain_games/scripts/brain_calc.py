#!/usr/bin/env python3
from brain_games.core import start_game_cycle

from brain_games.games.calc import create_game_round


def main():
    description = 'What is the result of the expression?'
    start_game_cycle(description, create_game_round, [])


if __name__ == '__main__':
    main()
