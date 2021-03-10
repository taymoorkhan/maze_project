# controllers/end.py
#from maze.views.game import PlayerSprite
from views.game import MazeBlock, Item,PlayerSprite, ExitSprite, StaticImages
from models.maze import Maze
from pygame import gfxdraw
import pygame
import pygame.locals
import math
# surface to follow player
# rectangle_surface = pygame.Surface((21, 21))

class GameController:

    """

    Takes the app window as a parameter and manipulates it with a collection of sprites `GameView`.

    :param window: Application Window
    :type window: <pygame.Surface>
    

    """


    def __init__(self, window):

        # initializes window to be used by controller
        self._window = window

        # initializes basic maze sprites from MazeBlock class and inserts into group
        self.maze_block = MazeBlock()
        self.blocks = pygame.sprite.Group()
        
        # initializes item sprites from Item class and inserts into group
        self.item = Item()
        self.items = pygame.sprite.Group()
        self.item_img = self.item.image

        # initializes player sprites from PlayerSprite class and inserts into group
        self.player = PlayerSprite()
        self.player_image = self.player.image
        self.img = self.maze_block.image
        
        # Gets maze and Player object from Maze model
        self.maze = Maze("models/grid_02.txt")
        self.model_player = self.maze._player

        # Creates a exit sprite group
        self.exits = pygame.sprite.Group()

        # Creates static images
        self._static = StaticImages()
        self._coins = self._static.coinshow()
        self._check = self._static.check()
        self._exit = self._static.exit()
        self._cross = self._static.cross()
        

    def display(self):
        """loop that is used to add to the sprite group for maze blocks
        """
      
        maze = self.maze.grid
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == "X":
                    self.createblocks(y,x)
           


    def displayPlayer(self):
        """[summary]loop to find the player location

        :return: [description]coorinates for player location
        :rtype: int
        """
        maze = self.maze.grid
        for x in range(len(maze)):
            for y in range(len(maze[x])):          
                if maze[x][y] =="P":
                    return x, y
                   

    # def additems(self):
    #     """adds the tokens to the item sprite group
    #     """
    #     self.maze.add_items()
    #     maze = self.maze.grid
    #     for x in range(len(maze)):
    #         for y in range(len(maze[x])):
    #             if maze[x][y] not in ["X", "P", "E", " "]:
                   
    #                 self.createitem(y,x)
    def additems(self):
        """adds the tokens to the item sprite group
        """
        itemlist = ['S','H','R','M', 'B', 'C']
        self.maze.add_items()
        maze = self.maze.grid
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] in itemlist:
                    itemvalue = maze[x][y]
                    itemlist.remove(itemvalue)
                    self.createitem(y,x)
                    


    def display_exit(self):
        """[summary]loop to find the exit location

        :return: [description]coordinates for exit location
        :rtype: int
        """
        maze = self.maze.grid
        for x in range(len(maze)):
            for y in range(len(maze[x])):          
                if maze[x][y] =="E":
                    self.exit_item(y,x) 
                                   

    def createblocks(self,y,x):
        """
        adds items to the self.blocks sprite group
        
        :param x: y coordinate
        :type x: int

        :param y: x coordinate
        :type y: int
    
        """
        block = MazeBlock()
        block.update(y,x)
        self.blocks.add(block)

    def createitem(self,y,x):
        """
        adds items to the self.items sprite group
        
        :param x: y coordinate
        :type x: int

        :param y: x coordinate
        :type y: int
    
        """   
        item = Item()
        item.update(y,x)
        self.items.add(item)


    def exit_item(self,y,x):
        """
        adds items to the self.exits sprite group
        
        :param x: y coordinate
        :type x: int

        :param y: x coordinate
        :type y: int
    
        """ 
        exit = ExitSprite()
        exit.update(y,x)
        self.exits.add(exit) 

         
        

    def loop(self):
        """
        This is the game loop, runs until a win or lose condition is fulfilled

        """
        # initiate pygame
        pygame.init()
        running = True
        # opens a display on top of window
        self.display()

        #black surface that covers player sprite's last location
        rectangle_surface = pygame.Surface((10, 10))
        
        # calls method to display player co-ordinates
        x, y = self.displayPlayer()

        # method to display the items
        self.additems()

        # finds location of exist and add to its sprite group
        self.display_exit()

        # uses the sprite group blocks to draw the walls
        self.blocks.draw(self._window) 

        # uses the sprite group to add the items
        self.items.draw(self._window)

        # uses sprite group for exit
        self.exits.draw(self._window)
        
        # ### Testing Background #######
        background_img = pygame.image.load("views/images/background.png").convert()
        background = pygame.transform.scale(background_img, (800, 600))
        # updates the player position
        self.player.rect.x = x*25 
        self.player.rect.y = y*25

        # initiates pygame display and clock
        pygame.display.update()
        clock = pygame.time.Clock()
        current_time = 4800
        font = pygame.font.SysFont('arial', 48)
        # begins the loop until game ends
        while running:
            clock.tick(50)
            current_time -= 1
            time_in_seconds = math.floor(current_time/80)

            if current_time == 0:
                return False, 0


            # if user clicks "X" on window, window closes
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    return "kill"


            # these are conditions if user uses the WASD controls. 
            # If the player collides with a wall, the game will push him the other way
            # If the player collides with an item, it will be added to his backpack
         
            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.changespeed(-4, 0)
                    elif event.key == pygame.K_d:
                        self.player.changespeed(4, 0)
                    elif event.key == pygame.K_w:
                        self.player.changespeed(0, -4)
                    elif event.key == pygame.K_s:
                        self.player.changespeed(0, 4)
 
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.changespeed(4, 0)
                    elif event.key == pygame.K_d:
                        self.player.changespeed(-4, 0)
                    elif event.key == pygame.K_w:
                        self.player.changespeed(0, 4)
                    elif event.key == pygame.K_s:
                        self.player.changespeed(0, -4)

            if pygame.sprite.spritecollide(self.player, self.exits, dokill=False): 

                #deletes all sprites
                for sprite in self.blocks.sprites():
                        del sprite
                for sprite in self.items.sprites():
                        del sprite
                for sprite in self.exits.sprites():
                        del sprite

                # # delivers win condition, if users backpack contains the four items, they win! return True
                if len(self.items) == 2:
                    return True, current_time
                elif len(self.items) == 1:
                    return True, current_time + 500

                elif len(self.items) == 0:
                    return True, current_time + 1000

                else:
                    return False, 0
                
               
            #covers the image blur of the player
            self.player.update(self.blocks,self.items)
            # updates the player position
            self._window.fill((0,0,0))

            ### Background and coins won blit ###
            self._window.blit(background, [0,0])
            self._window.blit(self._cross, (700, 625))
            if len(self.items) <= 5:
                self._window.blit(self._coins, (225, 625))
            if len(self.items) <= 4:
                self._window.blit(self._coins, (300, 625))
            if len(self.items) <= 3:
                self._window.blit(self._coins, (375, 625))
            if len(self.items) <=2:
                self._window.blit(self._coins, (450, 625))
                self._window.blit(self._check, (700, 625))
            if len(self.items) <=1:
                self._window.blit(self._coins, (525, 625))
            if len(self.items) <=0:
                self._window.blit(self._coins, (600, 625))
            
            
            self.blocks.draw(self._window)
            self.items.draw(self._window)
            self._window.blit(self.player_image,self.player.rect)
            # timer display
            if time_in_seconds >= 30:
                text = font.render (f"Timer: {str(time_in_seconds)}", True, (34,139,34))
            elif time_in_seconds >= 10:
                text = font.render (f"Timer: {str(time_in_seconds)}", True, (255,215,0))
            else:
                text = font.render (f"Timer: {str(time_in_seconds)}", True, (220,20,60))
            
            
            
            self._window.blit(text, (25, 625))

            # exit
            self._window.blit(self._exit, [775, 75])
            
            # updates window
            pygame.display.flip()
            pygame.display.update()
            self._window.convert()
        






