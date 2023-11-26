import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game_round(
    start: int = 0, stop: int = 100
) -> tuple[str, str]:
    a, b = _generate_expression(start, stop)

    question = f'{a} {b}'
    correct_answer = _get_correct_answer(a, b)

    return question, correct_answer


def _generate_expression(start: int, stop: int) -> tuple[int, int]:
    a = random.randrange(start, stop)
    b = random.randrange(start, stop)

    return a, b


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
