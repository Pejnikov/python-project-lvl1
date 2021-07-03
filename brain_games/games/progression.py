from random import randint
from brain_games.game_engine.games_logic import start_game


def get_brain_progression_data():
    FIELDS_COUNT = 10
    MIN_BORDER = 1
    MAX_BORDER = 20
    question = ''
    difference = randint(MIN_BORDER, MAX_BORDER)
    field_value = randint(0, MAX_BORDER)
    empty_field = randint(0, FIELDS_COUNT - 1)
    for field in range(FIELDS_COUNT):
        field_value += difference
        if field != empty_field:
            question += '{} '.format(str(field_value))
        else:
            answer = field_value
            question += '.. '
    return (question.strip(), answer)


def start_prog_game():
    game_rule = 'What number is missing in the progression?'
    start_game(game_rule, get_brain_progression_data)
