import random

from brain_games.core import start_game_cycle

_PROGRESSION_NUMBERS_COUNT_MIN = 5
_PROGRESSION_NUMBERS_COUNT_MAX = 15


def start_game():
    description = 'What number is missing in the progression?'
    start_game_cycle(
        description,
        _generate_progression,
        _get_correct_answer,
    )


def _generate_progression(
    start: int = 0,
    stop: int = 100,
    step_start: int = 1,
    step_stop: int = 10,
) -> tuple[str, tuple[int, int, int, int]]:
    progression_numbers_count = random.randrange(
        _PROGRESSION_NUMBERS_COUNT_MIN, _PROGRESSION_NUMBERS_COUNT_MAX
    )

    start_number = random.randrange(start, stop)
    step = random.randrange(step_start, step_stop)
    hidden_number_position = random.randrange(0, progression_numbers_count)

    answer_args = (
        start_number, step, progression_numbers_count, hidden_number_position
    )

    progression_numbers = []
    progression_iter = _yield_progression(
        start_number, step, progression_numbers_count
    )
    for i, number in enumerate(progression_iter):
        if i == hidden_number_position:
            progression_numbers.append("..")

        else:
            progression_numbers.append(str(number))

    return " ".join(progression_numbers), answer_args


def _get_correct_answer(
    start: int,
    step: int,
    numbers_count: int,
    hidden_number_position: int,
) -> str:
    for i, number in enumerate(_yield_progression(start, step, numbers_count)):
        if i == hidden_number_position:
            return str(number)


def _yield_progression(start: int, step: int, elements_count: int):
    number = start
    for _ in range(elements_count):
        yield number
        number += step


__all__ = ['start_game']
