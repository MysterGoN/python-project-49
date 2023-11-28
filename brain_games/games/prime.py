import random
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GENERATION_START_NUMBER = 0
GENERATION_STOP_NUMBER = 100000


def create_game_round() -> tuple[str, str]:
    number = _generate_random_number(
        GENERATION_START_NUMBER, GENERATION_STOP_NUMBER
    )

    question = f'{number}'
    answer = _get_correct_answer(number)

    return question, answer


def _generate_random_number(start: int, stop: int) -> int:
    number = random.randrange(start, stop)
    return number


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
