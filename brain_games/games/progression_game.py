from random import randint
from ..game_engine.games_logic import start_game


def get_brain_progression_data():
    sentence = ''
    length = 10
    min_rand_num = 1
    max_rand_num = 20
    diff = randint(min_rand_num, max_rand_num)
    cur_prog_val = randint(0, max_rand_num)
    qn_position = randint(0, length - 1)

    for cur_prog_position in range(length):
        cur_prog_val += diff
        if cur_prog_position != qn_position:
            sentence += '{} '.format(str(cur_prog_val))
        else:
            missed_member = cur_prog_val
            sentence += '.. '
    return (sentence.strip(), missed_member)


def start_prog_game():
    game_rule = 'What number is missing in the progression?'
    start_game(game_rule, get_brain_progression_data)
