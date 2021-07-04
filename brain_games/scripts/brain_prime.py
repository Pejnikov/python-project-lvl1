from brain_games.games.prime import get_brain_prime_data
from brain_games.games.prime import PRIME_RULE
from brain_games.game_engine.games_logic import start_game


def main():
    start_game(PRIME_RULE, get_brain_prime_data)


if __name__ == '__main__':
    main()
