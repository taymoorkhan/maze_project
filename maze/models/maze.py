"""
maze.py - Group assignment
Taymoor
Ijaz
Luke
"""
# import random and Player class
from random import randrange
from models.player import Player
POINT_OF_PLAYER = 'P'
POINT_OF_EXIT = 'E'


class Maze:
    """ 
    Nested list created from text file representing a maze
    :param filename: text file containing maze
    :type filename: string
    """
    
    def __init__(self, _filename):
        """
        Initialization of instance attributes
        """
        # -- open text file containing maze
        self.file = open(_filename, 'r')
        self._grid = []
        # -- initialize line_list and append into list
        line_list = []
        lines = self.file.readlines()
        for line in lines:
            line = line.strip('\n')
            line_list = [char for char in line]
            self._grid.append(line_list)
         # -- placing the player at the very start
        self._player = Player(1,2)
        self._grid[self._player._x][self._player._y] = POINT_OF_PLAYER
        self._grid[3][-1] = POINT_OF_EXIT
        
        

    # --- Rename the check method to can_move_to
        """ 
        :return: return False if the location is a wall, otherwise return True
        :rtype: bool
        """

    #--@classmethod doesnt need to be a class method likewise for every other class method
    def can_move_to(self, line_num, col_num):
        """
        Check if coordinate is an empty space or wall
        :param line_num: establishes line number in grid
        :type line_num: integer
        
        :param col_num: establishes column number in grid
        :type col_num: integer
        
        :return: False if coordinates are a wall, True if empty space
        :rtype: bool
        """
        # -- checks if the coordinate is an empty space
        if self._grid[line_num][col_num] == " ":
            return True
        else:
            return False
        
    def display(self):
        """
        Prints the grid on the screen
        """
        for line in self._grid:
            print("".join(line))


    def find_random_spot(self):
        """
        Finds a random open spot in the maze
        
        :return: coordinates for open spot
        :rtype: tuple
        """
        random_line_index = []
        random_col = 0
        random_col_index = 100

        # -- loops through maze and stops when it finds an open spot
        while random_col != " ":
            random_line_index = randrange(len(self._grid))
            random_col_index = randrange(len(self._grid[random_line_index]))
            random_col = self._grid[random_line_index][random_col_index]
        # -- returns the coordinates of the open spot
        coordinates = (random_line_index, random_col_index)
        return coordinates

    @property
    def grid(self):
        return self._grid

    #--add random items
    
    @grid.setter
    def grid(self, value):
        self._grid = value
    
    def add_items(self):
        """
        Adds random items to the maze
        """
        # -- item list
        item = ['S','H','R','M', 'B', 'C']
        # -- loops through item list and adds them to the maze
        for i in item:
            x_coordinate, y_coordinate = self.find_random_spot()
            self.grid[x_coordinate][y_coordinate] = i



   
    def is_item(self, x_coordinate, y_coordinate):
        """
        If the location requested is a random item, return True
        :param x_coordinate: x coordinate of the location requested
        :type x_coordinate: integer
        :param y_coordinate: y coordinate of the location requested
        :type y_coordinate: integer
        :return: return False if the location requested is not a random item, else return True
        :rtype: bool
        """
        if self.grid[x_coordinate][y_coordinate] == "X" or self.grid[x_coordinate][y_coordinate] == " " or self.grid[x_coordinate][y_coordinate] == POINT_OF_PLAYER or self.grid[x_coordinate][y_coordinate] == POINT_OF_EXIT:
            return False

        else:
            return True
    
    def player_location(self):
        """
        Tracks player locations, returns x and y coordinate
        """
        x = 0
        y = 0
        for line in self.grid:
            for i in line:
                if i == "P":
                    return x, y
                    
                y+=1
            x += 1
            y = 0

    
    def is_exit(self, x_coordinate, y_coordinate):
        """
        If the location requested is the exit, return True
        """
        if self.grid[x_coordinate][y_coordinate] == POINT_OF_EXIT:
            return True
        else:
            return False