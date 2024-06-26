import random
import os
import re

def check_play_status():
    valid_responses = ["yes", "no"]
    while True:
        try:
            response = input("Would you like to play again? (yes/no): ")
            if response.lower() not in valid_responses:
                raise ValueError("Yes or No only")

            if response.lower() == "yes":
                return True
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Thanks for playing!")
                exit()

        except ValueError as err:
            print(err)


def play_rps():
    play = True
    while play:
        os.system("cls" if os.name == "nt" else "clear")
        print("")
        print("Rock, Paper, Scissors - Shoot!")

        user_choice = input("Choose your weapon"
                            " ([R]ock, [P]aper, [S]cissors): ")

        if not  re.match("[RrPpSs]", user_choice):
            print("Please choose a letter:")
            print("[R]ock, [P]aper, [S]cissors")
            continue

        print(f"I choose: {user_choice}")

        choice = ["R", "P", "S"]
        opp_choice = random.choice(choice)

        print(f"I choose: {opp_choice}")

        if opp_choice == user_choice.upper():
            print("Tie!")
            play = check_play_status()
        elif opp_choice == "R" and user_choice.upper() == "S":
            print("Rock beats Scissors!, I win!")
            play = check_play_status()
        elif opp_choice == "P" and user_choice.upper() == "R":
            print("Paper beats Rock!, I win!")
            play = check_play_status()
        elif opp_choice == "S" and user_choice.upper() == "P":
            print("Scissors beats Paper!, I win!")
            play = check_play_status()
        else:
            print("You win!\n")
            play = check_play_status()

if __name__ == "__main__":
    play_rps()