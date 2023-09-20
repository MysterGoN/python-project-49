from typing import Any, Callable

import prompt

_DEFAULT_GAME_ROUNDS = 3


def create_game_rounds(
    game_round_generation_function: Callable[[Any, ...], tuple[str, str]],
    function_args: list[Any],
    rounds_count: int = _DEFAULT_GAME_ROUNDS,
) -> list[tuple[str, str]]:
    game_rounds = []
    for _ in range(rounds_count):
        game_rounds.append(game_round_generation_function(*function_args))

    return game_rounds


def start_game_cycle(
    rules_description: str,
    game_rounds: list[tuple[str, str]],
):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')

    print(rules_description)
    for question, correct_answer in game_rounds:
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {player_name}!")
            break

    else:
        print(f'Congratulations, {player_name}!')


__all__ = ['create_game_rounds', 'start_game_cycle']
