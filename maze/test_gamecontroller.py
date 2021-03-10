from controllers.game import GameController
import pytest

import pygame





def test_game_controller():
    assert hasattr(GameController, 'display')
    assert hasattr(GameController, 'displayPlayer') 