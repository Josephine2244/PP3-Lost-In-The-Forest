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

![Title](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/b137d357-c818-44cf-8d6e-71f08004366b)

### Add Name
The user adds their name at the beginning of the game to personalise the experience.

### End Game graphics

![End game input no](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/f584241a-be2b-4bb4-b85b-37a209f93ff4)

### Multiple paths with different choices
There are two paths the user can choose from. Each come with their own challenges and choices along the way.

### Colored text
Multiple colors are used to draw the attention of the player to important parts, e.g options, the riddle and the end of game.
- ![coloredtext1](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/49930f4d-c1a6-4413-a2a7-ccb2509ba5d7)
- ![coloredtext2](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/43a000f2-d5bb-4e19-9bb0-9f380e0d7686)
- ![coloredtext3](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/fdadaa61-69b0-4c79-8f9c-ea49898b4f17)

## Future Features
- Multiple difficulty levels
- A choice of game locations

## Typography and Color Scheme
- A large font is used to display the title at the beginning of the game to capture the users attention.
- Where users must input a choice to move forward, the options are presented in a green font so that they stand out to the user.
- A blue font is used to display the riddle so that it is clear to the user that it is separate from the story narration of the game.

## Flow Chart
![flowchart-raw](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/12764a8c-86df-4034-8f09-e605995eb031)

## Technology

- Python
- Github
- CodeAnywhere
- Heroku
- Lucid Chart
- Termcolor (ANSII color formatting installed in the workspace terminal)
- Art (ASCII Art for game title installed in the workspace terminal)

## Testing

### PEP8 Python Validator Results
![CI Python Linter Results](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/196e377e-a8f4-41bf-9165-d4363bcc7b00)

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
| 22 | Meet troll input 'fight' | Input 'fight' where prompted to do so | Input is accepted and leads to next scene (hit troll) |
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
| 52 | End game story | Check appearance of story | Story is easy to understand and is legible |
| 53 | End game play again input 'yes' | Input 'yes' where prompted to do so | Input is accepted and leads back to start game scene |
| 54 | End game play again input 'no' | Input 'no' where prompted to do so | Input is accepted and leads to end game screen |
| 55 | End game play again incorrect input | Input incorrect value when prompted to choose an option | Input is rejected. Player prompted to input choice again |

## 01
![Title](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/3a1d6432-0d0e-405d-996d-f754ea62fa7a)

## 02
![Start story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/72c6459f-03a6-4b39-9547-98454226303f)

## 03
![Name input](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/58e66787-dc4d-4c2d-bc2c-5a9516c5fe6a)

## 04
![Name input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/003e90d2-850b-418d-b9e5-0fcf46b122d6)

## 05
![First Challenge story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/80142084-3108-4dba-be32-4953b5fef608)

## 06
![First challenge input left](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/a30373fc-7681-4ddd-a7b7-b0c7c4a359aa)

## 07
![First challenge input right](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/ff828d61-4be4-4162-9186-bef21ea01e8b)

## 08
![First challenge input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/c5c72985-c104-4d92-9a23-2c4305c8089e)

## 09
![Cross bridge story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/2853d7a5-7385-4300-8f5e-1cb3842b49cd)

## 10
![Cross bridge input cross](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/7e69a3ad-81d6-43fe-bf5a-cf0954d82abb)

## 11
![Cross bridge input back](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/c435729e-b17c-41c7-b704-179569c7a37b)

## 12
![Cross bridge input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/744c5803-e602-403f-8551-5a13e5c96f8f)

## 13
![Tree down story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/4527e7ea-ee2d-4b93-81fb-8a6baf4e4360)

## 14
![Tree down input jump](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/617a7cc3-8fb8-4a2e-9ee8-5672128d3fc3)

## 15
![Tree down input back](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/a1708cb0-1842-4ffc-8142-afb01e2cc66b)

## 16
![Tree down input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/2036fc2a-1f8c-4e26-9aad-ce7e88fe09d6)

## 17
![Meet troll story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/ad3d8d2e-5bac-48b3-9f71-95613099b215)

## 18 & 19
![Meet troll riddle](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/57cea5b9-80c9-406b-90a6-87e10afb8037)

## 20
![Meet troll input answer](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/29e29b47-4756-4801-9440-2e19c84c3cb8)

## 21
![Meet troll riddle incorrect input](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/d6678fe6-a0f7-420c-a48f-3bebc8834200)

## 22
![Meet troll input fight](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/00494276-60ca-4a8e-84f3-a23fcf1f57f2)

## 23
![Meet troll input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/36621534-2855-46ca-b616-2eaa81031886)

## 24
![Meet troll input hit](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/244745cd-eeb7-4550-9ada-d38c4723c870)

## 25
![Meet troll input hit incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/f006d685-7c21-45b5-b02e-3aa75a126125)

## 26
![Get chased story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/ffe976d6-0400-414d-912d-ce97788a0588)

## 27
![Get chased input run](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/92c3268a-aaa3-43ee-9a6f-63496ce8a562)

## 28
![Get chased input hide](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/fdadd830-7957-473b-ba0c-3d48101ace8d)

## 29
![Get chased input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/20602735-660a-4b37-891d-8be0895c0f2a)

## 30
![Escape troll story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/96cf9bd6-99f4-4847-b0aa-242a9da4ef73)

## 31
![Escape troll input run](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/67a3f64b-8b79-4f9f-b444-58bc79cbba1c)

## 32
![Escape troll input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/d26fa326-bc3a-4bd3-8835-eedd96f5ee58)

## 33
![Meet goblin story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/e3cce281-b424-49d9-8b0c-3705f5b42595)

## 34
![Meet goblin input give](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/7bfa322c-1ed0-4090-a60c-347f9f8c6382)

## 35
![Meet goblin input fight](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/4603d42c-1ffd-4cec-b5a0-a08513bf2f29)

## 36
![Meet goblin input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/fef43a88-0b30-4f0a-9a91-ee8713b47512)

## 37
![Find map story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/5eab5f6e-4408-4cad-8d25-ff1e8095b34d)

## 38
![Find map input follow](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/346b3f53-e971-42d9-a957-0c61e9f92c9b)

## 39
![Find map input ignore](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/5611f2b0-6d46-45a0-b016-a8d2a21e0310)

## 40
![Find map input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/8437f90e-794c-44bc-9a0f-be2630c7b8e8)

## 41
![Enter forest story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/99bd0055-d3c6-4b02-9c85-228ea4b4a9f5)

## 42
![Enter forest input back](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/684b4647-0e0a-407e-ba07-ac5923b0707c)

## 43
![Enter forest input continue](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/afc9f261-3f75-4aab-8692-d7cea3cb2e3d)

## 44
![Enter forest input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/35dc09a1-3ab9-438e-bb65-5eee0ea42919)

## 45
![Exit forest story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/836829f1-a64f-4314-b311-113ac139bc18)

## 46
![Exit forest input run](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/076c6464-c690-4f6c-86b2-32a4a48f259a)

## 47
![Exit forest input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/e2da687a-05a0-413f-be05-26712b353410)

## 48
![Near end game story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/517d1ef8-d862-4775-8d10-435588ef6fd4)

## 49
![Near end game input investigate](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/7eee2dd5-fcd4-46d9-8644-983fbdd38d05)

## 50
![Near end game input explore](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/27bc2eea-977d-47f6-ac6b-1d875e627e2c)

## 51
![Near end game incorrect input](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/18e67a3a-b153-4901-9efd-47db2c7e3c74)

## 52
![End game story](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/a9a56eb9-3d78-4e4c-be6b-6eba5ce2ff4a)

## 53
![End game input yes](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/63e5c9dc-f4cf-4237-9d0d-20a0bb16d0f8)

## 54
![End game input no](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/ae07b722-029f-4615-bba2-07e127911242)

## 55
![End game input incorrect](https://github.com/Josephine2244/PP3-Lost-In-The-Forest/assets/137813807/13489e84-9a1a-4d8c-992d-5e5d9e15e797)

### Fixed bugs

- Game was not moving to next scene if input had to be re-entered. It was fixed by adding 'while true' to start of function and rearranging order of options in the function.
- run.py file very long and lots of print statements. I created a new file to separate the story segments and keep the run.py functions simple and readable.
- Lines to long in python code. Shortened const names and changed some statements into multiline statements.

## Deployment

### via CodeAnywhere
1. Log into Codeanywhere.
2. Go to workspace that was created for the project using link copied from Github.
3. Open workspace and go to terminal at bottom of page.
4. Type 'python3 run.py'
5. The python code will begin running in the terminal.

### via Heroku
1. Log into Heroku.
2. Create new app.
3. Assign it a name.
4. Go to settings tab.
5. Add 2 buildpacks: heroku/python, heroku/nodejs.
6. Ensure they are in this order. They can be dragged and dropped to change the order.
7. In Config Vars, add Key: PORT, Value: 8000.
8. Go to deploy tab and scroll down to 'Manual Deploy'.
9. Select 'Main' branch and click 'Deploy Branch'.
10. Once the app is built, a view button will appear.
11. Click 'view' and the app will open in a new tab.

### Forking project on Github
- Open Github and login.
- Go to the repository that you want forked.
- The fork button on on the top right side across from the repository name.

### Cloning project on Github
- Open Github and login
- Go to the repository you want to clone.
- Click the blue 'Code' button and it will give three options of how to clone the repository (HTTPS/SSH/Github CLI).
- Copy the URL
- In a new terminal, change current directory to the location you want for the clone directory.
- Type 'git clone' in the terminal followed by the URL you copied.

## Credits
- Instructions on adding colored text to terminal [here](https://dev.to/dev_neil_a/python-how-to-adding-color-and-styles-to-terminal-text-3699)
- Instructions on installing termcolor [here](https://pypi.org/project/termcolor/)
- Instructions on installing termcolor [here](https://pypi.org/project/art/)
- My Mentor, Rohit, for all his advice throughout the project.
