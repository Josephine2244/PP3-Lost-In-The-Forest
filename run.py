"""
This is the main game play. The functions bring the players
from scene to scene depending on their choices along the way.
"""
from art import *
from termcolor import colored
from storytext import *

tprint("Lost In The Forest", font="small")


def end_game():
    """
    Gives player choice to play again or end the game.
    """
    while True:
        print("Do you want to play again?")
        print(colored("Options: yes/no", "green"))
        final_choice = input()
        if final_choice not in directions:
            print("Please enter a valid option.")
        elif final_choice == "yes":
            start_game()
        else:
            print("Thank you for playing!")
            tprint("The End", font="big")
            print("Created by: @josephine2244")


def after_goblin():
    """
    This function allows the player to choose to leave the forest
    or choose to keep exploring. If they choose to keep exploring
    they get to complete the goblin challenge.
    """
    while True:
        print(AFTER_GOBLIN_AND_TROLL)
        print(colored("Options: investigate/explore", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "explore":
            cross_bridge()
        elif player_choice == "investigate":
            print(f"Congratulations {name}! You are out of the forest!")
            end_game()


def after_troll():
    """
    This function allows the player to choose to leave the forest
    or choose to keep exploring. If they choose to keep exploring
    they get to complete the goblin challenge.
    """
    while True:
        print(AFTER_GOBLIN_AND_TROLL)
        print(colored("Options: investigate/explore", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "investigate":
            print(f"Congratulations {name}! You are out of the forest!")
            end_game()
        elif player_choice == "explore":
            tree_down()


def meet_goblin():
    """
    This is the goblin challenge. The player must fight the
    goblin or give it their cloak.
    """
    while True:
        print(MEET_GOBLIN_STORY)
        print(colored("Options: give cloak/fight\n", "green"))
        player_choice = input()
        if player_choice not in directions:
            print("Please enter a valid option.")
        elif player_choice == "give cloak":
            print("Success! The goblin takes the cloak and leaves.\n")
            print(f"Let's get moving {name} before we freeze!")
            after_goblin()
        elif player_choice == "fight":
            print(FIGHT_GOBLIN)
            print(f"Success {name}! You grab your cloak and run!\n")
            after_goblin()


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
    player_choice = take_user_input(TREE_DOWN_STORY, TREE_DOWN_INPUTS)
    TREE_DOWN_INPUTS[player_choice]()


def cross_bridge():
    """
    This function sets up the scene for the troll challenge.
    It also gives the player the choice to go back and pick
    a different direction.
    """
    player_choice = take_user_input(CROSS_BRIDGE_STORY, CROSS_BRIDGE_INPUTS)
    CROSS_BRIDGE_INPUTS[player_choice]()


def first_challenge():
    """
    This is the first choice of the game.
    This will decide which challenge they face.
    """
    player_choice = take_user_input(FIRST_CHALLENGE_STORY, FIRST_CHALLENGE_INPUTS)
    FIRST_CHALLENGE_INPUTS[player_choice]()


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


def print_options_text(keys):
    """
    This function prints the options available to the player.
    """
    display_text = "Options: "
    key_index = 0
    for key in keys:
        if key_index == 0:
            display_text += key
        else:
            display_text += "/" + key
        key_index+=1
    print(colored(display_text, "green"))


def take_user_input(first_print, input_options):
    """
    This function takes the user input and checks if it is valid
    """
    while True:
        print(first_print)
        print_options_text(input_options.keys())
        player_choice = input()
        player_choice = player_choice.lower()
        if player_choice in input_options:
            return player_choice
        else:
            print("Please enter a valid option.")


FIRST_CHALLENGE_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
CROSS_BRIDGE_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
TREE_DOWN_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
MEET_GOBLIN_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
FIGHT_GOBLIN_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
FIND_MAP_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
ENTER_DARK_FOREST_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
EXIT_DARK_FOREST_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
GET_CHASED_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
ESCAPE_TROLL_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
NEAR_END_GAME_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
END_GAME_INPUTS = {'left' : tree_down, 'right' : cross_bridge}
ANSWER = ["coin", "a gold coin", "a coin", "gold coin"]

if __name__ == '__main__':
    start_game()
