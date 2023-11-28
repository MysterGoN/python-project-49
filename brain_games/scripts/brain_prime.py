#!/usr/bin/env python3
from brain_games.core import start_game_cycle

from brain_games.games import prime


def main():
    start_game_cycle(prime)


if __name__ == '__main__':
    main()
