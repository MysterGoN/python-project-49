import operator
import random

from brain_games.core import start_game_cycle, create_game_rounds

_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

_OPERATORS = list(_OPERATIONS.keys())


def start_game():
    description = 'What is the result of the expression?'
    game_rounds = create_game_rounds(_create_game_round, [])

    start_game_cycle(
        description,
        game_rounds,
    )


def _create_game_round(
    start: int = 0, stop: int = 100
) -> tuple[str, str]:
    global _OPERATIONS

    a, b, operation = _generate_expression(start, stop)

    question = _create_a_question(a, b, operation)
    correct_answer = _get_correct_answer(a, b, operation)

    return question, correct_answer


def _generate_expression(start: int, stop: int) -> tuple[int, int, str]:
    global _OPERATORS

    a = random.randrange(start, stop)
    b = random.randrange(start, stop)
    operation = random.choice(_OPERATORS)

    return a, b, operation


def _create_a_question(a: int, b: int, operation: str) -> str:
    return f'{a} {operation} {b}'


def _get_correct_answer(a: int, b: int, operation: str) -> str:
    global _OPERATIONS

    return str(_OPERATIONS[operation](a, b))


__all__ = ['start_game']
