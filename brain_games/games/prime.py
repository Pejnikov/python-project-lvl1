from random import randint
from math import sqrt


PRIME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divider in range(2, 1 + int(sqrt(number))):
        if number % divider == 0:
            return False
    return True


def get_brain_prime_data():
    MIN_BORDER = 1
    MAX_BORDER = 3571
    question = randint(MIN_BORDER, MAX_BORDER)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)
