#!/usr/bin/env python3
from brain_games.core import start_game_cycle

from brain_games.games.gcd import create_game_round


def main():
    description = 'Find the greatest common divisor of given numbers.'
    start_game_cycle(description, create_game_round, [])


if __name__ == '__main__':
    main()
