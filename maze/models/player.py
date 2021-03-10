"""
player.py - Group assignment
Taymoor
Ijaz
Luke
"""



class Player:
    """
    Contains an attribute named backpack that will store the random items picked up
    :param_ _backpack: Object used to store random items
    :rtype: object
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialization of instance attributes
        """
        self._backpack = []
        self._x = x_coordinate
        self._y = y_coordinate
        pass
    
    # getter and setter for backpack
    @property
    def backpack(self):
        return self._backpack

    @backpack.setter
    def backpack(self, value):
        self._backpack = value
    