import prompt

_DEFAULT_GAME_ROUNDS = 3


def start_game_cycle(game_module):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')

    print(game_module.DESCRIPTION)
    for _ in range(_DEFAULT_GAME_ROUNDS):
        question, correct_answer = game_module.create_game_round()
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
