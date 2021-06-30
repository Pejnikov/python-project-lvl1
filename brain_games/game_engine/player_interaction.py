from prompt import string


def welcome_player(rule):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rule)
    return name


def get_ans_to_qn(qn_string):
    print('Question: {}'.format(qn_string))
    answer = string('Your answer: ')
    return answer


def print_game_result(pl_name, is_winner):
    if is_winner:
        print("Congratulations, {}!".format(pl_name))
    else:
        print("Let's try again, {}!".format(pl_name))
