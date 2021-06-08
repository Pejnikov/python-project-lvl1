from brain_games.games.common import ask_qn

QUESTIONS_COUNT = 3
MIN_RAND_NUM = 1
MAX_RAND_NUM = 100


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
