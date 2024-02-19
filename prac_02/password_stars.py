USER_PASSWORD = "LIUSIYI"


def get_password():
    min_length = 7
    password = input("Please enter your password:")

    while len(password) < min_length:
        print("Invalid password. Remember, password must be at least 7 characters long.")
        password = input("Please enter your password:")

    return password


def print_password_asterisks(password):
    print("*" * len(password))


def main():
    password = get_password()
    print_password_asterisks(password)


if __name__ == "__main__":
    main()
