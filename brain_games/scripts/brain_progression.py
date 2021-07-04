from brain_games.games.progression import get_brain_progression_data
from brain_games.games.progression import PROGRESSION_RULE
from brain_games.game_engine.games_logic import start_game


def main():
    start_game(PROGRESSION_RULE, get_brain_progression_data)


if __name__ == '__main__':
    main()
