from random import randint
from brain_games.game_engine.games_logic import start_game
from brain_games.game_engine.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_even_data():
    rand_num = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    is_even = 'yes' if rand_num % 2 == 0 else 'no'
    return (rand_num, is_even)


def start_even_game():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(game_rule, get_brain_even_data)
