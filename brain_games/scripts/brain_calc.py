#!/usr/bin/env python3
from brain_games.core import start_game_cycle

from brain_games.games import calc


def main():
    start_game_cycle(calc.DESCRIPTION, calc.create_game_round, [])


if __name__ == '__main__':
    main()
