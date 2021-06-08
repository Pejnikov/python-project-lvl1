from random import randint, choice
from brain_games.games.common import welcome_player, print_game_result
from brain_games.games.games_logic import is_game_winner
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


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


def main():
    game_rule = 'What is the result of the expression?'
    pl_name = welcome_player(game_rule)
    winner_flag = is_game_winner(get_brain_calc_data)
    print_game_result(pl_name, winner_flag)


if __name__ == '__main__':
    main()
