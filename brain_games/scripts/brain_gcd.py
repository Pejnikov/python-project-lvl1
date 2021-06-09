from random import randint
from math import gcd
from brain_games.games.common import welcome_player, print_game_result
from brain_games.games.games_logic import is_game_winner
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_gcd_data():
    number_1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    number_2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    qn_string = '{} {}'.format(number_1, number_2)
    answ = gcd(number_1, number_2)
    return(qn_string, answ)


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    pl_name = welcome_player(game_rule)
    winner_flag = is_game_winner(get_brain_gcd_data)
    print_game_result(pl_name, winner_flag)


if __name__ == '__main__':
    main()
