from random import randint
from math import sqrt
from brain_games.games.common import welcome_player, print_game_result
from brain_games.games.games_logic import is_game_winner
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def is_prime(number):
    for i in range(2, 1 + int(sqrt(number))):
        if number % i == 0:
            return False
    return True


def get_brain_prime_data():
    random_number = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    answer = 'yes' if is_prime(random_number) else 'no'
    return (random_number, answer)


def main():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    pl_name = welcome_player(game_rule)
    winner_flag = is_game_winner(get_brain_prime_data)
    print_game_result(pl_name, winner_flag)


if __name__ == '__main__':
    main()
