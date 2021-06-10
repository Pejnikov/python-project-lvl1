from random import randint
from math import gcd
from brain_games.games.games_logic import start_game
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_gcd_data():
    number_1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    number_2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    qn_sentence = '{} {}'.format(number_1, number_2)
    answ = gcd(number_1, number_2)
    return(qn_sentence, answ)


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    start_game(game_rule, get_brain_gcd_data)


if __name__ == '__main__':
    main()
