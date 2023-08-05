import random

from brain_games.core import start_game_cycle

_ADD = "+"
_SUB = "-"
_MUL = "*"

_ALLOWED_OPERATIONS = [_ADD, _SUB, _MUL]


def start_game():
    description = 'What is the result of the expression?'
    start_game_cycle(
        description,
        _generate_expression,
        _get_correct_answer,
    )


def _generate_expression(
    start: int = 0, stop: int = 100
) -> tuple[str, tuple[int, int, str]]:
    global _ALLOWED_OPERATIONS

    a = random.randrange(start, stop)
    b = random.randrange(start, stop)
    operation = random.choice(_ALLOWED_OPERATIONS)

    return f"{a} {operation} {b}", (a, b, operation)


def _get_correct_answer(a: int, b: int, operation: str) -> str:
    global _ADD, _SUB, _MUL

    if operation == _SUB:
        answer = _sub(a, b)

    elif operation == _MUL:
        answer = _mul(a, b)

    else:
        answer = _add(a, b)

    return str(answer)


def _add(a: int, b: int) -> int:
    return a + b


def _sub(a: int, b: int) -> int:
    return a - b


def _mul(a: int, b: int) -> int:
    return a * b


__all__ = ['start_game']
