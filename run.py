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
        print(colored("You have escaped the forest!\n", "red"))
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


def near_end_game():
    """
    This function gives the player the choice to end the game by investigating
    the opening or keep exploring. If they choose to keep exploring they will
    be brought back to the beginning so they can choose an alternate path.
    """
    player_choice = take_user_input(NEAR_END_GAME_STORY, NEAR_END_GAME_INPUTS)
    NEAR_END_GAME_INPUTS[player_choice]()


def exit_dark_forest():
    """
    This function brings the dark forest scene to an end and leads to the
    end game scene.
    """
    player_choice = take_user_input(EXIT_DARK_FOREST_STORY, EXIT_DARK_FOREST_INPUTS)
    EXIT_DARK_FOREST_INPUTS[player_choice]()


def enter_forest():
    """
    This function sets up the scene for the dark forest and gives the player
    the option to return to the find map scene.
    """
    player_choice = take_user_input(ENTER_DARK_FOREST_STORY, ENTER_FOREST_INPUTS)
    ENTER_FOREST_INPUTS[player_choice]()


def find_map():
    """
    This function gives the player the option to follow the map
    they find or to ignore it and find their own way.
    """
    player_choice = take_user_input(FIND_MAP_STORY, FIND_MAP_INPUTS)
    FIND_MAP_INPUTS[player_choice]()


def escape_troll():
    """
    This function gives the player the chance to run away after the
    troll runs past them.
    """
    player_choice = take_user_input(ESCAPE_TROLL_STORY, ESCAPE_TROLL_INPUTS)
    ESCAPE_TROLL_INPUTS[player_choice]()


def get_chased():
    """
    This function gives the player the option to run or hide when being
    chased by the troll.
    """
    player_choice = take_user_input(GET_CHASED_STORY, GET_CHASED_INPUTS)
    GET_CHASED_INPUTS[player_choice]()


def fight_goblin():
    """
    This function plays out the story of the fight and allows the player
    to continue to the next scene.
    """
    player_choice = take_user_input(FIGHT_GOBLIN_STORY, FIGHT_GOBLIN_INPUTS)
    FIGHT_GOBLIN_INPUTS[player_choice]()


def meet_goblin():
    """
    This is the goblin challenge. The player must fight the
    goblin or give it their cloak.
    """
    player_choice = take_user_input(MEET_GOBLIN_STORY, MEET_GOBLIN_INPUTS)
    MEET_GOBLIN_INPUTS[player_choice]()


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
            if player_answer not in ANSWER:
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


FIRST_CHALLENGE_INPUTS = {'left': tree_down, 'right': cross_bridge}
CROSS_BRIDGE_INPUTS = {'cross': meet_troll, 'back': first_challenge}
TREE_DOWN_INPUTS = {'jump': meet_goblin, 'back': first_challenge}
MEET_GOBLIN_INPUTS = {'give': find_map, 'fight': fight_goblin}
FIGHT_GOBLIN_INPUTS = {'continue': find_map}
FIND_MAP_INPUTS = {'follow': end_game, 'ignore': enter_forest}
ENTER_FOREST_INPUTS = {'back': find_map, 'continue': exit_dark_forest}
EXIT_DARK_FOREST_INPUTS = {'run': end_game}
GET_CHASED_INPUTS = {'run': end_game, 'hide': escape_troll}
ESCAPE_TROLL_INPUTS = {'run': near_end_game}
NEAR_END_GAME_INPUTS = {'investigate': end_game, 'explore': first_challenge}
END_GAME_INPUTS = {'yes': start_game, 'no': end_game}
ANSWER = ["coin", "a gold coin", "a coin", "gold coin"]

if __name__ == '__main__':
    start_game()
