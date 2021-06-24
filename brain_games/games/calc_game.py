from random import randint, choice
from ..game_engine.games_logic import start_game


def get_brain_calc_data():
    min_rand_num = 1
    max_rand_num = 15
    operand_1 = randint(min_rand_num, max_rand_num)
    operand_2 = randint(min_rand_num, max_rand_num)
    possible_operators = '+-*'
    cur_operator = choice(possible_operators)
    qn_sentence = '{} {} {}'.format(operand_1, cur_operator, operand_2)
    if cur_operator == possible_operators[0]:
        answ = operand_1 + operand_2
    elif cur_operator == possible_operators[1]:
        answ = operand_1 - operand_2
    elif cur_operator == possible_operators[2]:
        answ = operand_1 * operand_2
    else:
        raise ValueError
    return(qn_sentence, answ)


def start_calc_game():
    game_rule = 'What is the result of the expression?'
    start_game(game_rule, get_brain_calc_data)
