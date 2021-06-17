from random import randint
from brain_games.game_engine.games_logic import start_game
from brain_games.game_engine.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


def get_brain_gcd_data():
    number_1 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    number_2 = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    qn_sentence = '{} {}'.format(number_1, number_2)
    answ = gcd(number_1, number_2)
    return(qn_sentence, answ)


def start_gcd_game():
    game_rule = 'Find the greatest common divisor of given numbers.'
    start_game(game_rule, get_brain_gcd_data)
