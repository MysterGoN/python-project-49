import math
import random

from brain_games.core import start_game_cycle


def start_game():
    description = 'Find the greatest common divisor of given numbers.'
    start_game_cycle(
        description,
        _generate_expression,
        _get_correct_answer,
    )


def _generate_expression(
    start: int = 0, stop: int = 100
) -> tuple[str, tuple[int, int]]:
    a = random.randrange(start, stop)
    b = random.randrange(start, stop)
    return f"{a} {b}", (a, b)


def _get_correct_answer(a: int, b: int) -> str:
    gcd = _find_greatest_common_division(a, b)
    return str(gcd)


def _find_greatest_common_division(a: int, b: int) -> int:
    max_possible_division = min(a, b)

    gcd = 1
    for i in range(2, max_possible_division + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


__all__ = ['start_game']
