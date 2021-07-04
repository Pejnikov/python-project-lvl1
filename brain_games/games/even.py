from random import randint
from brain_games.game_engine.games_logic import start_game


def get_brain_even_data():
    MIN_BORDER = 1
    MAX_BORDER = 100
    question = randint(MIN_BORDER, MAX_BORDER)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)


def start_even_game():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(game_rule, get_brain_even_data)
