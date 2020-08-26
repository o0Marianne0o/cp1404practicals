MIN_LENGTH = 4


def main():
    password = get_password()

    print_asterisk(password)


def print_asterisk(password):
    print('*' * len(password))


def get_password():
    print("Password must be at least {} characters.".format(MIN_LENGTH))
    password = input("Enter desired password: ")
    while len(password) < MIN_LENGTH:
        print("your password must be at least {} characters. Try Again".format(MIN_LENGTH))
        password = input("Enter desired password: ")
    return password


main()
