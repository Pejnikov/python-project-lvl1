from random import randint, choice
from brain_games.common import ask_qn

QUESTIONS_COUNT = 3
MIN_RAND_NUM = 1
MAX_RAND_NUM = 100


def get_brain_even_data():
    random_number = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    is_even = 'yes' if random_number % 2 == 0 else 'no'
    return (random_number, is_even)


def get_brain_calc_data():
    number_1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    number_2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    possible_operators = '+-*'
    cur_operator = choice(possible_operators)
    qn_string = '{} {} {}'.format(number_1, cur_operator, number_2)
    if cur_operator == '+':
        answ = number_1 + number_2
    elif cur_operator == '-':
        answ = number_1 - number_2
    else:
        answ = number_1 * number_2
    return(qn_string, answ)


def perform_game(game, qn_count=QUESTIONS_COUNT):
    for i in range(qn_count):
        if 'brain_even' in game:
            (qn_data, exp_answ) = get_brain_even_data()
        elif 'brain_calc' in game:
            (qn_data, exp_answ) = get_brain_calc_data()
        else:
            print('Game doesn\'t exist')
            return False
        answ = ask_qn(qn_data)
        if str(answ) == str(exp_answ):
            print('Correct!')
        else:
            error_msg = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(error_msg.format(answ, exp_answ))
            return False
    return True
