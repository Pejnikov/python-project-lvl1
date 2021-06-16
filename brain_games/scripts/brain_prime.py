from random import randint
from math import sqrt
from brain_games.games.games_logic import start_game
from brain_games.games.games_logic import MIN_RAND_NUM, MAX_RAND_NUM


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, 1 + int(sqrt(number))):
        if number % i == 0:
            return False
    return True


def get_brain_prime_data():
    rand_num = randint(MIN_RAND_NUM, MAX_RAND_NUM)
    answer = 'yes' if is_prime(rand_num) else 'no'
    return (rand_num, answer)


def main():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_game(game_rule, get_brain_prime_data)


if __name__ == '__main__':
    main()
