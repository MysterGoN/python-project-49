#!/usr/bin/env python3
from brain_games.core import start_game_cycle

from brain_games.games import progression


def main():
    start_game_cycle(progression)


if __name__ == '__main__':
    main()
