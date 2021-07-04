from random import randint


GCD_RULE = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number2 != 0:
        temp = number1
        number1 = number2
        number2 = temp % number2
    return number1


def get_brain_gcd_data():
    MIN_BORDER = 1
    MAX_BORDER = 25
    number_1 = randint(MIN_BORDER, MAX_BORDER)
    number_2 = randint(MIN_BORDER, MAX_BORDER)
    question = '{} {}'.format(number_1, number_2)
    answer = gcd(number_1, number_2)
    return(question, answer)
