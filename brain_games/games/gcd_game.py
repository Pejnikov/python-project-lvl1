from random import randint
from ..game_engine.games_logic import start_game


def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


def get_brain_gcd_data():
    min_rand_num = 1
    max_rand_num = 25
    number_1 = randint(min_rand_num, max_rand_num)
    number_2 = randint(min_rand_num, max_rand_num)
    qn_sentence = '{} {}'.format(number_1, number_2)
    answ = gcd(number_1, number_2)
    return(qn_sentence, answ)


def start_gcd_game():
    game_rule = 'Find the greatest common divisor of given numbers.'
    start_game(game_rule, get_brain_gcd_data)
