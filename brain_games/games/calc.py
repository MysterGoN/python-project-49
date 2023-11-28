import operator
import random

DESCRIPTION = 'What is the result of the expression?'

_GENERATION_START_NUMBER = 0
_GENERATION_STOP_NUMBER = 100

_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}
_OPERATORS = list(_OPERATIONS.keys())


def create_game_round() -> tuple[str, str]:
    a = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)
    b = random.randrange(_GENERATION_START_NUMBER, _GENERATION_STOP_NUMBER)
    operation = random.choice(_OPERATORS)

    question = f'{a} {operation} {b}'
    correct_answer = str(_OPERATIONS[operation](a, b))

    return question, correct_answer
