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
    _welcome()
    player_name = _get_player_name()
    _greet_the_player(player_name)

    _show_game_rules(rules_description)
    for question, correct_answer in game_rounds:
        _ask_question(question)

        user_answer = _get_answer()
        if user_answer == correct_answer:
            _congrats_on_the_correct_answer()

        else:
            _print_lose_message(user_answer, correct_answer)
            _lets_try_again(player_name)
            break

    else:
        _congrats_on_winning_the_game(player_name)


def _welcome():
    print('Welcome to the Brain Games!')


def _get_player_name(prompt_text: str = 'May I have your name? ') -> str:
    return prompt.string(prompt_text)


def _greet_the_player(player_name: str):
    print(f'Hello, {player_name}!')


def _show_game_rules(rules_description: str):
    print(rules_description)


def _ask_question(text: Any):
    print(f'Question: {text}')


def _get_answer(prompt_text: str = 'Your answer: ') -> str:
    return prompt.string(prompt_text)


def _congrats_on_the_correct_answer():
    print('Correct!')


def _congrats_on_winning_the_game(player_name: str):
    print(f'Congratulations, {player_name}!')


def _print_lose_message(wrong_answer: str, correct_answer: str):
    print(
        f"'{wrong_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )


def _lets_try_again(player_name: str):
    print(f"Let's try again, {player_name}!")


__all__ = ['create_game_rounds', 'start_game_cycle']
