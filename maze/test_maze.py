import pytest
from models.maze import Maze



@pytest.fixture
def maze():
    """
    create instance of class Maze  to help with tests
    """
    return Maze('models/grid_02.txt')

def test_maze_constructor(maze):
    """
    ID: 1A
    test that a grid has been created
    """
    assert isinstance(maze._grid,list) # testing to see if the constructor returns a list

def test_method(maze):
    """
    ID: 2A
    test for attribute can_move_to
    """
    assert hasattr(maze,'can_move_to')


def test_grid_getter(maze):
    """
    ID: 3A
    test to see if a getter for grid has been correctly implemented
    """
    assert type(maze.__class__.grid) == property

def test_empty_space(maze):
    """
    ID: 4A
    test the boolean condition of empty space
    """
    assert not maze.can_move_to(1,2)
    assert maze.can_move_to(1, 1) 

def test_player_location(maze):
    """
    ID: 5A
    test to see if a player location is implemented
    """
    assert maze.player_location() == (1, 2)

def test_point_ext(maze):
    """
    ID: 6A
    Test that location of exit is being implemented
    """
    assert maze.is_exit(3,-1)
    assert not maze.is_exit(2,-1)



def test_always_item(maze):
    """
    ID: 7A
    """
    # Test to see if all items are placed in the grid
    for _ in range(5):
        searchList = []
        maze.add_items()
        for line in maze.grid:
            for chr in line:
                if chr == 'S' or chr =='H' or chr == 'M' or chr == 'R':
                    searchList.append(chr)
    # asserting these items have been put in the grid
        assert 'S' in searchList
        assert 'H' in searchList
        assert 'M' in searchList
        assert 'R' in searchList


def test_random_loop(maze):
    """
    ID: 8A
    Test to see if the loop to find a random spot actually gives us a ' ' space
    """
    for _ in range(5):
        newList = maze.grid # this is a copy of the list
        coordinates = maze.find_random_spot() # getting the co-ordinates to return
        x , y = coordinates # assigning co-ordinates to value
        assert  newList[x][y] == ' '# asserting that the co-ordinates returned are actually an empty space
        assert maze.can_move_to(x,y) # this will test that a return boolean of true is returned for the can_move_to()