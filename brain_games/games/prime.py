import random
from math import sqrt

from brain_games.core import start_game_cycle


def start_game():
    description = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    start_game_cycle(
        description,
        _generate_random_number,
        _get_correct_answer,
    )


def _generate_random_number(
    start: int = 0, stop: int = 100000
) -> tuple[str, tuple[int]]:
    number = random.randrange(start, stop)
    return str(number), (number,)


def _get_correct_answer(number: int) -> str:
    is_prime = _check_number_is_prime(number)
    answer = "yes" if is_prime else "no"
    return answer


def _check_number_is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, round(sqrt(number))):
        if number % i == 0:
            return False

    return True


__all__ = ['start_game']
