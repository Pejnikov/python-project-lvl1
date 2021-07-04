from random import randint


PROGRESSION_RULE = 'What number is missing in the progression?'


def get_progression(elenemts_count=10):
    MIN_BORDER = 1
    MAX_BORDER = 20
    difference = randint(MIN_BORDER, MAX_BORDER)
    element_value = randint(0, MAX_BORDER)
    progression = []
    for _ in range(elenemts_count):
        element_value += difference
        progression.append(element_value)
    return progression


def make_progression_holey(progression):
    progression_length = len(progression)
    if progression_length < 1:
        raise ValueError
    missed_position = randint(0, progression_length - 1)
    hole_value = progression[missed_position]
    progression[missed_position] = '..'
    return hole_value


def get_brain_progression_data():
    progression = get_progression()
    answer = make_progression_holey(progression)
    question = ' '.join(str(element) for element in progression)
    return (question, answer)
