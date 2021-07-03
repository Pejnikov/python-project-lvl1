from random import randint
from brain_games.game_engine.games_logic import start_game


def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


def get_brain_gcd_data():
    MIN_BORDER = 1
    MAX_BORDER = 25
    number_1 = randint(MIN_BORDER, MAX_BORDER)
    number_2 = randint(MIN_BORDER, MAX_BORDER)
    question = '{} {}'.format(number_1, number_2)
    answer = gcd(number_1, number_2)
    return(question, answer)


def start_gcd_game():
    game_rule = 'Find the greatest common divisor of given numbers.'
    start_game(game_rule, get_brain_gcd_data)
