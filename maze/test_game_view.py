from maze.views.game import ExitSprite, Item, MazeBlock, PlayerSprite
import pytest
import pygame
import pygame.locals
from views.game import *



@pytest.fixture
def playersprite():
    return PlayerSprite()

@pytest.fixture
def exitsprite():
    return ExitSprite()


      

def test_sprite(playersprite):
    """[summary] test the onstructor is returning the corect default values

    :param playersprite: instance
    :type playersprite: PlayerSprite
    """

    assert playersprite.rect.y == 2
    assert playersprite.rect.x == 1


def test_change_speed(playersprite):
    """[summary] test the changespeed method in the PlayerSprite class

    :param playersprite: instance
    :type playersprite: PlayerSprite
    """
    playersprite.changespeed(3,3)
    assert playersprite.change_x == 3
    assert playersprite.change_y == 3 
    assert not playersprite.change_x == 2

def test_movement(playersprite):
    """[summary] test the update method in the PlayerSprite class this is how the player moves arond the maze and stops from hitting walls 

    :param playersprite: instance
    :type playersprite: PlayerSprite
    """
    walls = pygame.sprite.Group()
    items = pygame.sprite.Group()
    playersprite.changespeed(3,0)
    playersprite.update(walls,items)

    assert playersprite.rect.y == 2
    assert playersprite.rect.x == 4

    playersprite.changespeed(0,3)
    playersprite.update(walls,items)
    assert playersprite.rect.y == 5
    assert playersprite.rect.x == 7



def test_update(exitsprite):
    """[summary] test the update method of ExitSprite that values of rect are changed to correct values

    :param exitsprite: instance
    :type exitsprite: ExiteSprite
    """
    exitsprite.update(1,1)

    assert exitsprite.rect.y == 25
    assert exitsprite.rect.x == 25


        
