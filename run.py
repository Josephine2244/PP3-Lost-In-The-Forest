"""
This is the main game play. The functions bring the players
from scene to scene depending on their choices along the way.
"""
from art import *
from termcolor import colored
from storytext import *

tprint("Lost In The Forest", font="big")


def meet_troll():
    """
    This is the troll challenge. The player must fight
    the troll or answer a riddle to get passed.
    """
    while True:
        print(MEET_TROLL_STORY)
        print(colored("Options: speak/fight\n", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "speak":
            print(colored(RIDDLE, "blue"))
            player_answer = input()
            if player_answer not in answer:
                print("Incorrect! Here's a hint:")
                print("2 words, 4 letters each. Think of money...\n")
            else:
                print("That's correct! Let's keep moving.")
                after_troll()
        elif player_choice == "fight":
            print("You have chosen to fight. Quick! Hit the troll!\n")
            print(colored("Options: hit troll", "green"))
            player_choice = input()
            if player_choice not in directions:
                print("Please enter a valid option.")
            elif player_choice == "hit troll":
                print(f"You beat the troll! Let's get out of here {name}!\n")
                after_troll()



def tree_down():
    """
    This function sets up the scene for the goblin challenge.
    It also gives the player the choice to go back and pick
    a different direction.
    """
    while True:
        print(TREE_DOWN_STORY)
        print(colored("Options: jump over/go back\n", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "jump over":
            meet_goblin()
        elif player_choice == "go back":
            first_challenge()


def cross_bridge():
    """
    This function sets up the scene for the troll challenge.
    It also gives the player the choice to go back and pick
    a different direction.
    """
    while True:
        print(CROSS_BRIDGE_STORY)
        print(colored("Options: cross/go back\n", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "cross":
            meet_troll()
        elif player_choice == "go back":
            first_challenge()

def first_challenge():
    """
    This is the first choice of the game.
    This will decide which challenge they face.
    """
    while True:
        print(FIRST_CHALLENGE_STORY)
        print(colored("Options: left/right\n", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice = "left":
            tree_down()
        elif player_choice == "right":
            cross_bridge()


def start_game():
    """
    This sets up the game for the player.
    They enter their name to personalise the experience.
    """
    while True:
        print(START_GAME_STORY)
        global name
        name = input("Enter your name: \n")
        print("Processing...\n")
        if name == "":
            print("You have not entered a name. Please try again.")
        else:
            print(f"{name}, great! Let's begin...\n")
            first_challenge()


if __name__ == '__main__':
    start_game()