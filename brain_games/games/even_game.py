from random import randint
from ..game_engine.games_logic import start_game


def get_brain_even_data():
    min_rand_num = 1
    max_rand_num = 100
    rand_num = randint(min_rand_num, max_rand_num)
    answ = 'yes' if rand_num % 2 == 0 else 'no'
    return (rand_num, answ)


def start_even_game():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(game_rule, get_brain_even_data)
