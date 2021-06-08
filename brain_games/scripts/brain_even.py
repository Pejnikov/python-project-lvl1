from random import randint
from brain_games.games.common import welcome_player, print_game_result
from brain_games.games.games_logic import is_game_winner
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def get_brain_even_data():
    random_number = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    is_even = 'yes' if random_number % 2 == 0 else 'no'
    return (random_number, is_even)


def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    pl_name = welcome_player(game_rule)
    winner_flag = is_game_winner(get_brain_even_data)
    print_game_result(pl_name, winner_flag)


if __name__ == '__main__':
    main()
