master_pwd = input("What is the master password: ")


def view() -> None:
    with open("passwords.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            user, pwd = line.rstrip().split("|")
            print(f"Username: {user}\nPassword: {pwd}")


def add() -> None:
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}|{pwd}\n")


def main() -> None:
    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (view/add)? press q to quit: ").lower()

        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode")
            continue


main()
