from random import randint, choice
from brain_games.games.games_logic import start_game
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_calc_data():
    operand_1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    operand_2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    possible_operators = '+-*'
    cur_operator = choice(possible_operators)
    qn_sentence = '{} {} {}'.format(operand_1, cur_operator, operand_2)
    if cur_operator == '+':
        answ = operand_1 + operand_2
    elif cur_operator == '-':
        answ = operand_1 - operand_2
    else:
        answ = operand_1 * operand_2
    return(qn_sentence, answ)


def main():
    game_rule = 'What is the result of the expression?'
    start_game(game_rule, get_brain_calc_data)


if __name__ == '__main__':
    main()
