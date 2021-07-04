from brain_games.games.gcd import get_brain_gcd_data
from brain_games.games.gcd import GCD_RULE
from brain_games.game_engine.games_logic import start_game


def main():
    start_game(GCD_RULE, get_brain_gcd_data)


if __name__ == '__main__':
    main()
