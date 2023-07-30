import prompt


def welcome():
    print("Welcome to the Brain Games!")


def get_player_name(prompt_text: str = "May I have your name? ") -> str:
    return prompt.string(prompt_text)


def get_answer(prompt_text: str = "Your answer: ") -> str:
    return prompt.string(prompt_text)


def greet_player(player_name: str):
    print(f"Hello, {player_name}!")


def congratulate_player(player_name: str):
    print(f"Congratulations, {player_name}!")


def lets_try_again(player_name: str):
    print(f"Let's try again, {player_name}!")
