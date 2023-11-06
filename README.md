<h1 align="center">Lost In The Forest</h1>
Lost in the Forest is a text-based adventure game. The player must choose what direction to take to get passed any obstacles in their way as they try and make their way out of the forest.

[View Live Project here]

## Table of Contents

- [User Stories](user-stories)
- [Features](features)
- [Future Features](future-features)
- [Typography and Color Scheme](typography-and-color-scheme)
- [Flow Chart](flow-chart)
- [Technology](technology)
- [Testing](testing)
- [Deployment](deployment)
- [Credits](credits)

## User Stories

- As a new user, I would like to be able to start the game easily.
- As a new user, I would like the controls of the game to be easy to understand and follow.
- As a new user, I would like to have multiple paths to take so the game is varied.

## Features

### Title
The title is displayed in a big font at the begninning of the game to draw the attention of the user.

### Add Name
The user adds their name at the beginning of the game to personalise the experience.

### Multiple paths with different choices
There are two paths the user can choose from. Each come with their own challenges and choices along the way.

## Future Features
- Multiple difficulty levels
- A choice of game locations

## Typography and Color Scheme
- A large font is used to display the title at the beginning of the game to capture the users attention.
- Where users must input a choice to move forward, the options are presented in a green font so that they stand out to the user.
- A blue font is used to display the riddle so that it is clear to the user that it is separate from the story narration of the game.

## Flow Chart

## Technology

- Python
- Github
- CodeAnywhere
- Heroku
- Lucid Charts
- Termcolor (ANSII color formatting installed in the workspace terminal)
- Art (ASCII Art for game title installed in the workspace terminal)

## Testing
### Test Cases
| ID | Test Subject | Steps Taken | Outcome Generated |
|----|--------------|-------------|-------------------|
| 01 | Title | Go to game and check appearance of title | Title is legible and is of appropriate sizing |
| 02 | Start game story | Check appearance and readability of the story | Story is easy to understand and is legible. Options are shown in green |
| 03 | Input name | Input name where prompted to do so | Game handles input and will move to next scene if it is acceptable |
| 04 | Incorrect input name (empty) | Attempt to proceed with empty name input | Game will ask player to provide a valid name | 
| 05 | First challenge story | Check appearance of story | Story is easy to understand and is legible |
| 06 | First challenge input 'left' | Input 'left' where prompted to do so | Input is accepted and leads to next scene (tree down) |
| 07 | First challenge input 'right' | Input 'right' where prompted to do so | Input is accepted and leads to next scene (cross bridge) |
| 08 | First challenge incorrect input | Input incorrect value when prompted to choose an option | Input rejected. Player prompted to input choice again |
| 09 | Cross bridge story | Check appearance of story  | Story is easy to understand and is legible |
| 10 | Cross bridge input 'cross' | Input 'cross' where prompted to do so | Input is accepted and leads to next scene (meet troll) |
| 11 | Cross bridge input 'back' | Input 'back' where prompted to do so | Input is accepted and leads back to previous scene (first challenge) |
| 12 | Cross bridge incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 13 | Tree down story | Check appearance of story | Story is easy to understand and is legible |
| 14 | Tree down input 'jump' | Input 'jump' where prompted to do so | Input is accepted and leads to next scene (meet goblin) |
| 15 | Tree down input 'back' | Input 'back' where prompted to do so | Input is accepted and leads back to previous scene (first challenge) |
| 16 | Tree down incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 17 | Meet troll story | Check appearance of story | Story is easy to understand and is legible |
| 18 | Meet troll input 'speak' | Input 'speak' where prompted to do so | Input is accepted and leads to next scene (riddle) |
| 19 | Meet troll riddle | Check appearance of riddle | Riddle is easy to read and understand, appears in blue text |
| 20 | Meet troll riddle correct answer | Input riddle answer where prompted to do so | Input is accepted and leads to next scene (near end game) |
| 21 | Meet troll riddle incorrect answer | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again and is shown hints |
| 22 | Meet troll 'fight' | Input 'fight' where prompted to do so | Input is accepted and leads to next scene (hit troll) |
| 23 | Meet troll incorrect input | Input incorrect value when prompted to chooce an option| Input is rejected. Player prompted to input choice again |
| 24 | Meet troll input 'hit' | Input 'hit' where prompted to do so | Input is accepted and leads to next scene (after troll) |
| 25 | Meet troll fight incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 26 | Get chased story | Check appearance of story | Story is easy to understand and is legible |
| 27 | Get chased input 'run' | Input 'run' where prompted to do so | Input is accepted and leads to next scene (end game) |
| 28 | Get chased input 'hide' | Input 'hide' where prompted to do so | Input is accepted and leads to next scene (escape troll) |
| 29 | Get chased incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 30 | Escape troll story | Check appearance of story | Story is easy to understand and is legible |
| 31 | Escape troll input 'run' | Input 'run' where prompted to do so | Input is accepted and leads to next scene (near end game) |
| 32 | Escape troll incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 33 | Meet goblin story | Check appearance of story | Story is easy to understand and is legible |
| 34 | Meet goblin input 'give' | Input 'give' where prompted to do so | Input is accepted and leads to next scene (find map) |
| 35 | Meet goblin input 'fight' | Input 'fight' where prompted to do so | Input is accepted, fight story is easy to read and understand, and leads to next scene (find map) |
| 36 | Meet goblin incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 37 | Find map story | Check appearance of story | Story is easy to understand and is legible |
| 38 | Find map input 'follow' | Input 'follow' where prompted to do so | Input is accepted and leads to next scene (end game) |
| 39 | Find map input 'ignore' | Input 'ignore' where prompted to do so | Input is accepted and leads to next scene (enter dark forest) |
| 40 | Find map incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 41 | Enter forest story | Check appearance of story | Story is easy to understand and is legible |
| 42 | Enter forest input 'back' | Input 'back' where prompted to do so | Input is accepted and leads to next scene (find map) |
| 43 | Enter forest input 'continue | Input 'continue' where prompted to do so | Input is accepted and leads to next scene (exit forest) |
| 44 | Enter forest incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 45 | Exit forest story | Check appearance of story | Story is easy to understand and is legible |
| 46 | Exit forest input 'run' | Input 'run' where prompted to do so | Input is accepted and leads to next scene (end game) |
| 47 | Exit forest incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 48 | Near end game story | Check appearance of story | Story is easy to understand and is legible |
| 49 | Near end game input 'investigate' | Input 'investigate' where prompted to do so | Input is accepted and leads to next scene (end game) |
| 50 | Near end game input 'explore' | Input 'explore' where prompted to do so | Input is accepted and leads to next scene (first challenge) |
| 51 | Near end game incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |
| 52 | End game play again input 'yes' | Input 'yes' where prompted to do so | Input is accepted and leads back to start game scene |
| 53 | End game play again input 'no' | Input 'no' where prompted to do so | Input is accepted and leads to end game screen |
| 54 | End game play again incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |

### Fixed bugs

- Game was not moving to next scene if input had to be re-entered. It was fixed by adding 'while true' to start of function and rearranging order of options in the function

## Deployment

### via CodeAnywhere
1. Log into Codeanywhere.
2. Go to workspace that was created for the project using link copied from Github.
3. Open workspace and go to terminal at bottom of page.
4. Type 'python3 -m http.server' to open a preview of browser.
5. A box will pop up in the bottom right corner of the screen when you can click to open the browser.
6. This will open in a new tab.

### via Heroku
1. Log into Heroku
2. 

## Credits
