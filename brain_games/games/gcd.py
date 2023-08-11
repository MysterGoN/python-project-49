import random

from brain_games.core import start_game_cycle, create_game_rounds


def start_game():
    description = 'Find the greatest common divisor of given numbers.'
    game_rounds = create_game_rounds(_create_game_round, [])

    start_game_cycle(
        description,
        game_rounds,
    )


def _create_game_round(
    start: int = 0, stop: int = 100
) -> tuple[str, str]:
    a, b = _generate_expression(start, stop)

    question = _create_a_question(a, b)
    correct_answer = _get_correct_answer(a, b)

    return question, correct_answer


def _generate_expression(start: int, stop: int) -> tuple[int, int]:
    a = random.randrange(start, stop)
    b = random.randrange(start, stop)

    return a, b


def _create_a_question(a: int, b: int) -> str:
    return f'{a} {b}'


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
