from brain_games.game_engine.player_interaction import ask_qn, welcome_player
from brain_games.game_engine.player_interaction import print_game_result
QUESTIONS_COUNT = 3
MIN_RAND_NUM = 1
MAX_RAND_NUM = 100


def start_game(rule, game_data):
    pl_name = welcome_player(rule)
    winner_flag = is_game_winner(game_data)
    print_game_result(pl_name, winner_flag)


def is_game_winner(get_game_data, qn_count=QUESTIONS_COUNT):
    for round in range(qn_count):
        (qn_data, exp_answ) = get_game_data()
        if not is_won_round(qn_data, exp_answ):
            return False
    return True


def is_won_round(question_data, exp_answer):
    answ = ask_qn(question_data)
    if str(answ) == str(exp_answer):
        print('Correct!')
        return True
    else:
        error_msg = "'{}' is wrong answer ;(. Correct answer was '{}'."
        print(error_msg.format(answ, exp_answer))
        return False
