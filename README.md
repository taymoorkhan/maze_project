## Maze Game
## Creators: Taymoor Khan, Luke Salmon, and Ijaz Hussain

## Description
A maze game created for ACIT 2515 class.
This game is developed using Pygame and implemented in an MVC.

**Project Structure:**
C:.
│   README.md
│
├───documentation
│       UML.pdf
│
└───maze
    │   app.py
    │   main.py
    │   test_gamecontroller.py
    │   test_game_view.py
    │   test_maze.py
    │   test_models_score.py
    │   test_models_scoremanager.py
    │   test_player.py
    │   test_view.py
    │   __init__.py
    │
    ├───controllers
    │       app.py
    │       end.py
    │       game.py
    │       start.py
    │
    ├───models
    │       grid_02.txt
    │       maze.py
    │       player.py
    │       score.py
    │       scores.json
    │       score_manager.py
    │       __init__.py
    │
    ├───static
    │   └───styles
    │           background2.jpg
    │           style.css
    │
    ├───templates
    │       index.html
    │
    └───views
        │   end.py
        │   game.py
        │   start.py
        │   __init__.py
        │
        └───images
                alexthekidd.jpg
                alexx.jpg
                background.png
                check.jpg
                collect.png
                cross.png
                end.png
                exit.jpg
                exit.png
                gem.png
                lose.jpg
                start.png
                win.jpg
                x.png

**Dependencies:**
* Python 3.0 or higher
* Virtual Environment
* Pygame
* Pytest
* Flask (API)
* Web Browser

**Running the Game:**

*1. Create and run a virtual environment in the directory.*

*2. Install the Pygame package by entering 'pip install pygame' in your Terminal.*

*3. Launch the game by calling 'python main.py' in your Terminal.*

**Controls:**
* W Key: Move up
* S Key: Move down
* A Key: Move left
* D Key: Move right
* L-click: Start game by clicking start button

**Viewing the Scoreboard:**

*1. Install Flask by entering 'pip install flask' in your Terminal.*

*2. Launch the server by running 'python app.py' in your Terminal.*

*3. Open your web browser and enter 'localhost:5000' into the URL bar.* 

*3. Press ctrl + c in the Terminal to quit the server once you are finished viewing the page.* 

**Testing the Game:**

*1. Install Pytest by entering 'pip install pytest' in your Terminal.*

*2. Run the test files located in the root of the maze folder ie. 'python -m pytest test_maze.py'*

