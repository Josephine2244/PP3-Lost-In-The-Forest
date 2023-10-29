"""
Contains all the story segments for the game.
"""
directions = ["left", "right", "cross", "go back", "jump over",
              "speak", "fight", "hit troll", "give cloak", "fight",
              "investigate", "explore", "yes", "no"]

START_GAME_STORY = """Welcome to the Forest.
The aim of the game is to find your way out.
Each choice you make will decide the challenges you will face."""

FIRST_CHALLENGE_STORY = """You enter through the gate.
Do you want to go left or right?"""

CROSS_BRIDGE_STORY = """You come to a bridge.
To continue, you must cross the bridge or go back."""

TREE_DOWN_STORY = """Oh no! There is a tree blocking your path.
What will you do? Jump over it or go back?"""

MEET_TROLL_STORY = """A troll blocks your path.
Do you want to speak to the troll ot fight?"""

RIDDLE = """If you solve the riddle he will let you through.
The riddle is:
I have a gold head,
A gold tail,
But no body,
What am I?"""

answer = ["coin", "gold coin", "a coin", "a gold coin"]

MEET_GOBLIN_STORY = """You are greeted by an angry goblin.
He demands payment before you continue.
The only thing you have to give is your cloak.
You can give the goblin your cloak or fight it."""

FIGHT_GOBLIN = """You pretend to hand the goblin your cloak.
Instead you throw it over its head!
It is disorientated so you take your chance.
You grab a nearby branch and hit it.
It falls to the ground and you hear a soft snore."""

AFTER_GOBLIN_AND_TROLL = """You get passed and see an opening in the trees.
Will you investigate the opening or keep exploring?"""