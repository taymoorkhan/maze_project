import pytest
from models.player import Player

@pytest.fixture
def player():
    return Player(0,1)


def test_constructor(player):
    """
    ID: 1B
    This will test the constructor for valid return types
    """
    assert player._x == 0
    assert player._y == 1
    assert player.backpack == []


def test_backpack(player):
    """
    ID: 2B
    test the backpack property
    """
    assert type(player.__class__.backpack) == property

def test_backpack_length(player):
    """
    ID: 3B
    Test to see correct return value
    """
    assert len(player.backpack) == 0

def test_adding_to_backpack(player):
    """
    ID: 4B
    testing the setter for backpack
    """
    player.backpack = 'x'
    assert player.backpack[0] =='x'
    assert len(player.backpack) == 1



def test_x_property(player):
    """
    ID: 6B
    test for correct return value of getter
    """
    assert player._x == 0




def test_y_property(player):
    """
    ID: 9B
    test correct return values for y getter
    """
    assert player._y == 1

def test_setter_y(player):
    """
    ID: 10B
    test the setter for y co-ordinate
    """
    player._y = 2
    assert player._y == 2
