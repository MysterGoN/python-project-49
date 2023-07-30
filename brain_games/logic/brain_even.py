import random
from enum import StrEnum

from brain_games.logic import core

_GAME_ROUNDS = 3


class Answer(StrEnum):
    YES = "yes"
    NO = "no"


def start_game():
    core.welcome()
    player_name = core.get_player_name()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(_GAME_ROUNDS):
        number = _generate_random_number()
        print(f"Question: {number}")
        answer = core.get_answer()
        correct_answer = _get_correct_answer(number)

        if answer == correct_answer:
            print("Correct!")

        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            core.lets_try_again(player_name)
            break

    else:
        core.congratulate_player(player_name)


def _get_correct_answer(number: int) -> Answer:
    is_even = _check_number_is_even(number)

    return Answer.YES if is_even else Answer.NO


def _generate_random_number(start: int = 0, stop: int = 100) -> int:
    return random.randrange(start, stop)


def _check_number_is_even(number: int) -> bool:
    return number % 2 == 0
