"""
This is the main game play. The functions bring the players
from scene to scene depending on their choices along the way.
"""
from art import *
from termcolor import colored
from storytext import *

tprint("Lost In The Forest", font="big")


def start_game():
    """
    This sets up the game for the player.
    They enter their name to personalise the experience.
    """