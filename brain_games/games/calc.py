import operator
import random

DESCRIPTION = 'What is the result of the expression?'

_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

_OPERATORS = list(_OPERATIONS.keys())


def create_game_round(
    start: int = 0, stop: int = 100
) -> tuple[str, str]:
    a, b, operation = _generate_expression(start, stop)

    question = f'{a} {operation} {b}'
    correct_answer = _get_correct_answer(a, b, operation)

    return question, correct_answer


def _generate_expression(start: int, stop: int) -> tuple[int, int, str]:
    a = random.randrange(start, stop)
    b = random.randrange(start, stop)
    operation = random.choice(_OPERATORS)

    return a, b, operation


def _get_correct_answer(a: int, b: int, operation: str) -> str:
    return str(_OPERATIONS[operation](a, b))
