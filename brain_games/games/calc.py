from random import randint, choice
from brain_games.game_engine.games_logic import start_game


def get_brain_calc_data():
    MIN_BORDER = 1
    MAX_BORDER = 15
    PLUS = '+'
    MINUS = '-'
    MULTIPLICATION = '*'
    operand_1 = randint(MIN_BORDER, MAX_BORDER)
    operand_2 = randint(MIN_BORDER, MAX_BORDER)
    possible_operators = '{}{}{}'.format(PLUS, MINUS, MULTIPLICATION)
    operator = choice(possible_operators)
    question = '{} {} {}'.format(operand_1, operator, operand_2)
    if operator == PLUS:
        answer = operand_1 + operand_2
    elif operator == MINUS:
        answer = operand_1 - operand_2
    elif operator == MULTIPLICATION:
        answer = operand_1 * operand_2
    else:
        raise ValueError
    return(question, answer)


def start_calc_game():
    game_rule = 'What is the result of the expression?'
    start_game(game_rule, get_brain_calc_data)
