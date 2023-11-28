import random

DESCRIPTION = 'What number is missing in the progression?'

_GENERATION_START_NUMBER = 0
_GENERATION_STOP_NUMBER = 100
_START_NUMBER_OF_STEP_GENERATION = 1
_STOP_NUMBER_OF_STEP_GENERATION = 10

_PROGRESSION_NUMBERS_COUNT_MIN = 5
_PROGRESSION_NUMBERS_COUNT_MAX = 15


def create_game_round() -> tuple[str, str]:
    start_number = random.randrange(
        _GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER
    )
    step = random.randrange(
        _START_NUMBER_OF_STEP_GENERATION, _STOP_NUMBER_OF_STEP_GENERATION
    )
    progression_numbers_count = random.randrange(
        _PROGRESSION_NUMBERS_COUNT_MIN, _PROGRESSION_NUMBERS_COUNT_MAX
    )

    arithmetic_progression = _create_arithmetic_progression(
        start_number, step, progression_numbers_count
    )

    progression_length = len(arithmetic_progression)
    hidden_number_position = random.randrange(0, progression_length)
    hidden_progression = _create_hidden_progression(
        arithmetic_progression, hidden_number_position
    )

    question = ' '.join(hidden_progression)
    correct_answer = str(arithmetic_progression[hidden_number_position])

    return question, correct_answer


def _create_arithmetic_progression(
    start_number: int,
    step: int,
    numbers_count: int,
) -> list[int]:
    res = []
    for i in range(numbers_count):
        res.append(start_number + i * step)

    return res


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
