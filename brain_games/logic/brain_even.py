import random
from enum import Enum

from brain_games.logic.core import start_game_cycle


class Answer(Enum):
    YES = "yes"
    NO = "no"


def start_game():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game_cycle(
        description,
        _generate_random_number,
        _get_correct_answer,
    )


def _get_correct_answer(number: int) -> str:
    is_even = _check_number_is_even(number)
    answer = Answer.YES if is_even else Answer.NO
    return answer.value


def _generate_random_number(
    start: int = 0, stop: int = 100
) -> tuple[str, tuple[int]]:
    number = random.randrange(start, stop)
    return str(number), (number,)


def _check_number_is_even(number: int) -> bool:
    return number % 2 == 0


__all__ = ['start_game']
