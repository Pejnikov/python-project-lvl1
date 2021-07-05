from prompt import string


ROUNDS_COUNT = 3


def start_game(rule, get_game_data):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rule)
    winner = is_game_winner(get_game_data)
    if winner:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


def is_game_winner(get_game_data, rounds_count=ROUNDS_COUNT):
    for _ in range(rounds_count):
        (question, expected_answer) = get_game_data()
        print('Question: {}'.format(question))
        answer = string('Your answer: ')
        if str(answer) == str(expected_answer):
            print('Correct!')
        else:
            error_message = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(error_message.format(answer, expected_answer))
            return False
    return True
