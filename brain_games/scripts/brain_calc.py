from brain_games.games.calc import get_brain_calc_data
from brain_games.games.calc import CALC_RULE
from brain_games.games_engine import start_game


def main():
    start_game(CALC_RULE, get_brain_calc_data)


if __name__ == '__main__':
    main()
