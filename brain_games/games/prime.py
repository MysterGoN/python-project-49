import random
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

_GENERATION_START_NUMBER = 0
_GENERATION_STOP_NUMBER = 100000


def create_game_round() -> tuple[str, str]:
    number = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)

    question = f'{number}'
    correct_answer = 'yes' if _check_number_is_prime(number) else 'no'

    return question, correct_answer


def _check_number_is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, round(sqrt(number))):
        if number % i == 0:
            return False

    return True
