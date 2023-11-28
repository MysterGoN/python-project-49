import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

_GENERATION_START_NUMBER = 0
_GENERATION_STOP_NUMBER = 100


def create_game_round() -> tuple[str, str]:
    a = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)
    b = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)

    question = f'{a} {b}'
    correct_answer = str(_find_greatest_common_division(a, b))

    return question, correct_answer


def _find_greatest_common_division(a: int, b: int) -> int:
    max_possible_division = min(a, b)

    gcd = 1
    for i in range(2, max_possible_division + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd
