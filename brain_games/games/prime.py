import random
from math import sqrt

from brain_games.core import start_game_cycle, generate_game_rounds


def start_game():
    description = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    game_rounds = generate_game_rounds(_create_game_round, [])

    start_game_cycle(
        description,
        game_rounds,
    )


def _create_game_round(
    start: int = 0, stop: int = 100000
) -> tuple[str, str]:
    number = _generate_random_number(start, stop)

    question = _create_a_question(number)
    answer = _get_correct_answer(number)

    return question, answer


def _generate_random_number(start: int, stop: int) -> int:
    number = random.randrange(start, stop)
    return number


def _create_a_question(number: int) -> str:
    return f'{number}'


def _get_correct_answer(number: int) -> str:
    is_prime = _check_number_is_prime(number)
    answer = 'yes' if is_prime else 'no'
    return answer


def _check_number_is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, round(sqrt(number))):
        if number % i == 0:
            return False

    return True


__all__ = ['start_game']
