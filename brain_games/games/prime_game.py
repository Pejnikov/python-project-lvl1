from random import randint
from math import sqrt
from ..game_engine.games_logic import start_game


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, 1 + int(sqrt(number))):
        if number % i == 0:
            return False
    return True


def get_brain_prime_data():
    min_rand_num = 1
    max_rand_num = 3571
    rand_num = randint(min_rand_num, max_rand_num)
    answer = 'yes' if is_prime(rand_num) else 'no'
    return (rand_num, answer)


def start_prime_game():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_game(game_rule, get_brain_prime_data)
