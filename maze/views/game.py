# views/game.py
# Game class view page

# import necessary pygame tools
import pygame
import pygame.locals
import itertools
from models.maze import Maze

class MazeBlock(pygame.sprite.Sprite):
    """Creates a maze block sprite on the page"""

    def __init__(self):
        super().__init__()

        image = pygame.image.load('views/images/x.png')
        self.image = pygame.transform.scale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self,x,y):
        """[summary]method used to display the players position

        :param x: x coordinate
        :type x: int
        :param y: y coordinate
        :type y: int
        """

        self.rect.x = x*25
        self.rect.y = y*25

class Item(pygame.sprite.Sprite):
    """Creates item sprite on the page"""

    def __init__(self):
        super().__init__()

        image = pygame.image.load('views/images/gem.png')
        self.image = pygame.transform.scale(image, (15, 15))
        self.rect = self.image.get_rect()

    def update(self,x,y):
        """[summary]method used to display the item position

        :param x: x coordinate
        :type x: int
        :param y: y coordinate
        :type y: int
        """

        self.rect.x = x*25
        self.rect.y = y*25  

       


# end of original
class PlayerSprite(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        image = pygame.image.load('views/images/alexx.jpg')
        self.image = pygame.transform.scale(image, (18, 18))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = 2
        self.rect.x = 1
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None


    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self,walls,item):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)

        item_hit_list =  pygame.sprite.spritecollide(self, item, True)


        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class ExitSprite(pygame.sprite.Sprite): 
    """Creates sprite exit on the page"""

    def __init__(self):
        super().__init__()

        image = pygame.image.load('views/images/exit.png')
        self.image = pygame.transform.scale(image, (25, 25))
        self.rect = self.image.get_rect()
    
    def update(self,x,y):
        """[summary]method used to disply the exit position

        :param x: x coordinate
        :type x: int
        :param y: y coordinate
        :type y: int
        """

        self.rect.x = x*25
        self.rect.y = y*25  

class StaticImages:

    def __init__(self):
        pass


    def coinshow(self):
        image = pygame.image.load('views/images/collect.png').convert()
        coin_image = pygame.transform.scale(image, (60, 60))
        return coin_image

    def check(self):
        image = pygame.image.load('views/images/check.jpg').convert()
        check_image = pygame.transform.scale(image, (60, 60))
        return check_image

    def exit(self):
        image = pygame.image.load('views/images/exit.jpg').convert()
        exit_image = pygame.transform.scale(image, (25, 25))
        return exit_image

    def cross(self):
        image = pygame.image.load('views/images/cross.png').convert()
        cross_image = pygame.transform.scale(image, (60, 60))
        return cross_image


