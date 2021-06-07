from brain_games.common import welcome_player, print_game_result
from brain_games.games_logic import perform_game


def main():
    pl_name = welcome_player()
    print('What is the result of the expression?')
    is_winner = perform_game(__name__)
    print_game_result(pl_name, is_winner)


if __name__ == '__main__':
    main()
