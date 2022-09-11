import random

default_option = 3
run = True
invalid = True


def validate_input_user(data_obtained):
    if 0 < data_obtained < 5:
        return True
    else:
        return False


def get_selection_option(user_option):
    switcher = {
        1: "You choice rock",
        2: "You choice paper",
        3: "You choice scissors",
        4: "You choice exit"
    }

    return switcher.get(user_option, "invalid choice")


def get_computer_option(computer_option):
    switcher = {
        1: "Computer select rock",
        2: "Computer select paper",
        3: "Computer select scissors",
    }

    return switcher.get(computer_option, "invalid choice")


def compare_selections(computer_option, user_option):
    if user_option == computer_option:
        print("Draw")
    elif user_option == 4:
        print("Exit")
        exit()
    else:
        if user_option == 1 and computer_option == 3:
            print("You win")
        elif user_option == 1 and computer_option == 2:
            print("You lose")
        elif user_option == 2 and computer_option == 1:
            print("You win")
        elif user_option == 2 and computer_option == 3:
            print("You lose")
        elif user_option == 3 and computer_option == 2:
            print("You win")
        elif user_option == 3 and computer_option == 1:
            print("You lose")
        else:
            print("Invalid selection")


if __name__ == "__main__":
    while run:
        print("SELECT YOUR OPTION")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        try:
            input_user = int(input("Enter your choice: "))
            if validate_input_user(input_user):
                default_option = random.randint(1, 3)
                compare_selections(default_option, input_user)
                print("=====================================")
                print(get_selection_option(input_user))
                print("=====================================")
                print("===============Result================")
                print(compare_selections(default_option, input_user))
                print("===========Wanna Try Again?==========")
                print("1. Yes")
                print("2. No")
                while invalid:
                    try:
                        input_wanna_play = int(input("Your Answer: "))
                        if input_wanna_play == 1:
                            run = True
                        elif input_wanna_play == 2:
                            run = False
                            print("Thanks for playing")
                        else:
                            print("Invalid number")
                        invalid = False
                    except ValueError:
                        print("Please enter a valid option")
                        continue
            else:
                print("Invalid number")

        except ValueError:
            print("Invalid input")
            continue
