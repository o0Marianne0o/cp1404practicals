def user_name(email_address):
    split_email = email_address.split("@", 1)
    # print(split_email)
    users_name = split_email[0]
    split_name = users_name.split(".", 1)
    # print(split_name)
    join_name = " ".join(split_name)
    name = join_name.title()
    return name


def name_item(user_dict):
    for name, email in user_dict.items():
        print("{} ({})".format(name, email))


def main():
    email_address = input("Enter your email: ")
    user_dict = {}

    while email_address != "":
        name = user_name(email_address)
        user_ans = input("Is your name {}? (Y/n)".format(name)).lower()
        if not user_ans or user_ans[0] == "y":
            user_dict[email_address] = name
        elif user_ans[0] == "n":
            real_name = input("Name: ")
            name = user_name(real_name)
            user_dict[email_address] = name
        else:
            print("Invalid input. Try again")
        email_address = input("Enter your email: ")
    print(user_dict)
    print(name_item(user_dict))


main()