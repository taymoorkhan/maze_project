#controllers/end.py
#End class controller page

# import Endview
from views.end import EndView


# End Menu Controller

class EndController:
    """
    Takes the app window as a parameter and manipulates it with text and sprite from the view
    Uses `EndView`.

    :param window: Application Window
    :type window: <pygame.Surface>

    """
    def __init__(self, window):
        # initializes public attribute view which is a EndView object
        # uses window from app and image from EndView
        self.view = EndView()
        self._window = window
        self._img = self.view.image


    def display(self, condition, score):
        """
        blits end menu text and the sprite "end.png" button from EndView
        """

        # sends True or False to end menu view to display if user won or lost the game
        # currently only have showing true
        background = self.view.show_end_background(condition)
        self._window.blit(background, (0, 0))
        menu = self.view.show_end_menu(condition, score)
        self._window.blit(menu, (75, 75))   
        self._window.blit(self._img, self.view.rect)

    

    
