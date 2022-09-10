default_option = 3


def get_selection_option(input_user):
    switcher = {
        1: "You choice rock",
        2: "You choice paper",
        3: "You choice scissors",
        4: "You choice exit"
    }

    return switcher.get(input_user, "invalid choice")


def get_computer_option(default_option):
    switcher = {
        1: "Computer select rock",
        2: "Computer select paper",
        3: "Computer select scissors",
    }

    return switcher.get(default_option, "invalid choice")


def compare_selections(default_option, input_user):
    if input_user == default_option:
        print("Draw")
    else:
        if (input_user == 1 and default_option == 3):
            print("You win")
        elif (input_user == 1 and default_option == 2):
            print("You lose")
        elif (input_user == 2 and default_option == 1):
            print("You win")
        elif (input_user == 2 and default_option == 3):
            print("You lose")
        elif (input_user == 3 and default_option == 2):
            print("You win")
        elif (input_user == 3 and default_option == 1):
            print("You lose")


if __name__ == "__main__":
    print("SELECT YOUR OPTION")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    input_user = int(input("Enter your choice: "))

    print(get_selection_option(input_user))
    print(get_computer_option(default_option))
    print(compare_selections(default_option, input_user))
