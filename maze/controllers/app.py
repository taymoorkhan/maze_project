# controllers/end.py
# import pygame and required controllers
import datetime
import pygame
import pygame.locals
from controllers.start import StartController
from controllers.end import EndController
from controllers.game import GameController
from models.score_manager import ScoreManager
from models.score import Score
from flask import Flask, request


app = Flask(__name__)

score_manager = ScoreManager()

class App:
    """
    This is the app class. It manipulates the controllers and opens the window
    until the game ends.  
    """
    
    def __init__(self):
        pass
      

    def run(self):
        """
        This is the main method for our application.

        It runs an infinite loop, unless the user decides to quit or the game ends
        """

        # initiate pygame
        # initiates pygame clock
        pygame.init()
        pygame.display.set_caption('Kidd World')
        pygame.font.init()
        clock = pygame.time.Clock()

        # open a basic 800x600 pixel window and fill with white background
        window = pygame.display.set_mode((800, 700))
        window.fill((255, 255, 255))

        # runs window until it ends
        running = True

        # initiates start_page maze, and end_page views from controllers with window as a parameter to manipulate
        start_page = StartController(window)
        end_page = EndController(window)
        game_page = GameController(window)



        # begins by displaying start page
        start_page.display()


        # adds views/sprites to the sprite group
        sprite_group = pygame.sprite.Group()
        sprite_group.add(start_page.view)
        sprite_group.add(end_page.view)



        #Initiate Score and ScoreManager instances
        player = Score(0)
        manager = ScoreManager()
        
        while running:
            # game's fps
            clock.tick(50)

            # deletes a sprite if the sprite is not alive
            for sprite in sprite_group.sprites():
                if not sprite.alive():
                    del sprite


            # loop running to check for events in pygame
            for event in pygame.event.get():

                # checks if user clicked X on top right, if so, close window
                if event.type == pygame.locals.QUIT:
                    running = False

                # mouse click event, x and y are coordinates of the click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    # checks if start sprite is in sprite group
                    if start_page.view in sprite_group:

                        # if the start sprite is still in group and clicked, then it moves to the next page
                        if start_page.view.rect.collidepoint(x, y):
                            # removes start from the sprites so it can't be called again
                            sprite_group.remove(start_page.view)
                            window.fill((0, 0, 0))

                            #runs the game loop through game controller and view, collects win condition when game ends
                            condition, score = game_page.loop()


                            #------------------------------------------------------

                            player._score = score

                            # Create date variable for the day and time the game is played
                            x = datetime.datetime.now()
                            date = x.strftime("%x") 
                            time = x.strftime("%X")

                            #---------------------------------------------------------


                            # if x is pressed on game, condition returns kill and window closes
                            if condition == "kill":
                                running == False
                            else:
                                #colors page white with win/loss reply
                                #----------------------------------------------------------------------
                                if condition:
                                    background_image = pygame.image.load('views/images/win.jpg').convert()
                                    window.blit(background_image, (0, 0))
                                    impact_large = pygame.font.SysFont('impact', 60)
                                    congratulations = impact_large.render("Congratulations you won!", True, (107, 140, 255))
                                    window.blit(congratulations, (75, 75))
                                    impact_small = pygame.font.SysFont('impact', 40)
                                    second_line = impact_small.render("Please enter your name in the console.", True, (107, 140, 255))
                                    window.blit(second_line, (100, 500))
                                    pygame.display.update()
                                    player._name = [input('PLEASE ENTER PLAYER NAME '), date, time]
                                    manager.from_json()
                                    manager.add_score(player, True)
                                    manager.to_json()

                                #----------------------------------------------------------------------
                                window.fill((255, 255, 255))
                                end_page.display(condition, score)
                    
                    # if the end view sprite is clicked, then closes the application
                    elif end_page.view.rect.collidepoint(x,y):
                        running = False

            pygame.display.update()