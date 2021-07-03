from prompt import string


def start_game(rule, game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rule)
    winner = is_game_winner(game)
    if winner:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


def is_game_winner(get_game_data, questins_count=3):
    for _ in range(questins_count):
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
