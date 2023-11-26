import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_game_round(
    start: int = 0, stop: int = 100
) -> tuple[str, str]:
    number = _generate_random_number(start, stop)

    question = f'{number}'
    correct_answer = _get_correct_answer(number)

    return question, correct_answer


def _generate_random_number(start: int, stop: int) -> int:
    return random.randrange(start, stop)


def _get_correct_answer(number: int) -> str:
    is_even = _check_number_is_even(number)
    answer = 'yes' if is_even else 'no'
    return answer


def _check_number_is_even(number: int) -> bool:
    return number % 2 == 0
