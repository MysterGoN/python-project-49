from typing import Any, Callable

import prompt

_DEFAULT_GAME_ROUNDS = 3


def start_game_cycle(
    rules_description: str,
    question_generation_func: Callable[[], tuple[str, tuple[Any, ...]]],
    answer_generation_func: Callable[[Any, ...], str],
    *,
    game_rounds: int = _DEFAULT_GAME_ROUNDS,
):
    _welcome()
    player_name = _get_player_name()
    _greet_player(player_name)
    _show_game_rules(rules_description)

    for _ in range(game_rounds):
        question, question_args = question_generation_func()
        _ask_question(question)

        user_answer = _get_answer()
        correct_answer = answer_generation_func(*question_args)

        if user_answer == correct_answer:
            print("Correct!")

        else:
            _print_lose_message(user_answer, correct_answer)
            _lets_try_again(player_name)
            break

    else:
        _congratulate_player(player_name)


def _welcome():
    print("Welcome to the Brain Games!")


def _get_player_name(prompt_text: str = "May I have your name? ") -> str:
    return prompt.string(prompt_text)


def _greet_player(player_name: str):
    print(f"Hello, {player_name}!")


def _show_game_rules(rules_description: str):
    print(rules_description)


def _ask_question(text: Any):
    print(f"Question: {text}")


def _get_answer(prompt_text: str = "Your answer: ") -> str:
    return prompt.string(prompt_text)


def _congratulate_player(player_name: str):
    print(f"Congratulations, {player_name}!")


def _print_lose_message(wrong_answer: str, correct_answer: str):
    print(
        f"'{wrong_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )


def _lets_try_again(player_name: str):
    print(f"Let's try again, {player_name}!")


__all__ = ['start_game_cycle']
