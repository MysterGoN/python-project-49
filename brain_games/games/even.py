import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

_GENERATION_START_NUMBER = 0
_GENERATION_STOP_NUMBER = 100


def create_game_round() -> tuple[str, str]:
    number = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)

    question = f'{number}'
    number_is_even = number % 2 == 0
    correct_answer = 'yes' if number_is_even else 'no'

    return question, correct_answer
