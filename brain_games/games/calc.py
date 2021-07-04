from random import randint, choice


CALC_RULE = 'What is the result of the expression?'


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
