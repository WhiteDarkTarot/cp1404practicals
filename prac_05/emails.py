def extract_name(email):
    username = email.split("@")[0]
    parts = username.split(".")
    capitalized_parts = [part.capitalize() for part in parts]
    return " ".join(capitalized_parts)


def store_user_data():
    user_data = {}
    email = input("Email: ")
    while email:
        name = extract_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if name_confirmation in ["", "y"]:
            user_data[email] = name
        else:
            name = input("Name: ").strip()
            user_data[email] = name
        email = input("Email: ")

    return user_data


def main():
    user_data = store_user_data()
    for email, name in user_data.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
