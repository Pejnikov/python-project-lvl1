from brain_games.common import welcome_player, print_game_result
from brain_games.games_logic import perform_game


def main():
    pl_name = welcome_player()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_winner = perform_game(__name__)
    print_game_result(pl_name, is_winner)


if __name__ == '__main__':
    main()
