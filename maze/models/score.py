class Score:
    """ Simple class to represent a score in a game """

    def __init__(self,score,name = 'Player'):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score
        
    # Give name and score public property attributes
    @property
    
    def name(self):
        return self._name
        
    @property
    def score(self):
        return self._score
    
     
    def to_dict(self):
        """
        Returns a dict version of the class

        :return dict: Dictionary containing name as key, score as value
        :rtype: dict
        """
        return {"name": self._name, "score": self._score}



