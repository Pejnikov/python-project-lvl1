from brain_games.game_engine.player_interaction import get_ans_to_qn, welcome_player
from brain_games.game_engine.player_interaction import print_game_result


def start_game(rule, game):
    pl_name = welcome_player(rule)
    winner_flag = is_game_winner(game)
    print_game_result(pl_name, winner_flag)


def is_game_winner(get_game_data, qn_count=3):
    for _ in range(qn_count):
        (qn_data, exp_answ) = get_game_data()
        answ = get_ans_to_qn(qn_data)
        if str(answ) == str(exp_answ):
            print('Correct!')
        else:
            error_msg = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(error_msg.format(answ, exp_answ))
            return False
    return True
