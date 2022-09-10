default_option = "scissors"

def get_selection_option(input_user):
    switcher = {
        1: "you choice rock",
        2: "you choice paper",
        3: "you choice scissors",
        4: "you choice exit"
    }

    return switcher.get(input_user, "invalid choice")

if __name__ == "__main__":
    print("SELECT YOUR OPTION")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    input_user = input("Enter your choice: ")

    print(get_selection_option(input_user))


    if input_user == default_option:
        print("Draw")
    elif input_user == "rock":
        print("You win")
    elif input_user == "paper":
        print("You lose")
    elif input_user == "exit":
        print("Exit")




