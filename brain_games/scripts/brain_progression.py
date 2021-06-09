from random import randint
from brain_games.games.common import welcome_player, print_game_result
from brain_games.games.games_logic import is_game_winner
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_progression_data():
    prog_string = ''
    length = 10
    diff = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    cur_prog_val = randint(0, MAX_RAND_NUM)
    qn_position = randint(0, length - 1)

    for cur_prog_position in range(length):
        cur_prog_val += diff
        if cur_prog_position != qn_position:
            prog_string += '{} '.format(str(cur_prog_val))
        else:
            missed_member = cur_prog_val
            prog_string += '.. '
    return (prog_string.strip(), missed_member)


def main():
    game_rule = 'What number is missing in the progression?'
    pl_name = welcome_player(game_rule)
    winner_flag = is_game_winner(get_brain_progression_data)
    print_game_result(pl_name, winner_flag)


if __name__ == '__main__':
    main()
