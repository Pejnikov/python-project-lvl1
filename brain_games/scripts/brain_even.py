from brain_games.games.even import get_brain_even_data
from brain_games.games.even import EVEN_RULE
from brain_games.games_engine import start_game


def main():
    start_game(EVEN_RULE, get_brain_even_data)


if __name__ == '__main__':
    main()
