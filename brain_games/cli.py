from prompt import string


def welcome_user():
    name = string('May I have your name? ')
    print('Hello, {}!'.format(name))


def main():
    welcome_user()


if __name__ == '__main__':
    main()
