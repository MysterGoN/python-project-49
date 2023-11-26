import random

DESCRIPTION = 'What number is missing in the progression?'

_PROGRESSION_NUMBERS_COUNT_MIN = 5
_PROGRESSION_NUMBERS_COUNT_MAX = 15


def create_game_round(
    start: int = 0,
    stop: int = 100,
    step_start: int = 1,
    step_stop: int = 10,
) -> tuple[str, str]:
    progression = _generate_progression(start, stop, step_start, step_stop)

    hidden_number_position = _chose_hidden_number_position(len(progression))
    hidden_progression = _create_hidden_progression(
        progression, hidden_number_position
    )

    question = _create_a_question(hidden_progression)
    correct_answer = _get_correct_answer(progression, hidden_number_position)

    return question, correct_answer


def _generate_progression(
    start: int,
    stop: int,
    step_start: int,
    step_stop: int,
) -> list[int]:
    start_number = random.randrange(start, stop)
    step = random.randrange(step_start, step_stop)
    progression_numbers_count = random.randrange(
        _PROGRESSION_NUMBERS_COUNT_MIN, _PROGRESSION_NUMBERS_COUNT_MAX
    )

    arithmetic_progression = _create_arithmetic_progression(
        start_number, step, progression_numbers_count
    )
    return arithmetic_progression


def _create_arithmetic_progression(
    start_number: int,
    step: int,
    numbers_count: int,
) -> list[int]:
    res = []
    for i in range(numbers_count):
        res.append(start_number + i * step)

    return res


def _chose_hidden_number_position(progression_length: int) -> int:
    return random.randrange(0, progression_length)


def _create_hidden_progression(
    progression: list[int],
    hidden_number_position: int,
) -> list[str]:
    hidden_number_symbol = '..'

    hidden_progression = []
    for i, number in enumerate(progression):
        if i == hidden_number_position:
            hidden_progression.append(hidden_number_symbol)

        else:
            hidden_progression.append(str(number))

    return hidden_progression


def _create_a_question(hidden_progression: list[str]) -> str:
    return ' '.join(hidden_progression)


def _get_correct_answer(
    progression: list[int],
    hidden_number_position: int,
) -> str:
    hidden_number = progression[hidden_number_position]
    return f'{hidden_number}'
