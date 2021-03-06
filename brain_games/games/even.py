from random import randint


EVEN_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_BORDER = 1
MAX_BORDER = 100


def get_brain_even_data():
    question = randint(MIN_BORDER, MAX_BORDER)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)
