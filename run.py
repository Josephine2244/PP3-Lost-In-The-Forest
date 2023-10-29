"""
This is the main game play. The functions bring the players
from scene to scene depending on their choices along the way.
"""
from art import *
from termcolor import colored
from storytext import *

tprint("Lost In The Forest", font="big")


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