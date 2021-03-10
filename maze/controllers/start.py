#controllers/start.py
#Start class controller page

# import Startview
from views.start import StartView

# Start menu Controller


class StartController:
    """
    Takes the app window as a parameter and manipulates it with text and sprite from the view
    Uses `StartView`.

    :param window: Application Window
    :type window: <pygame.Surface>

    """
    def __init__(self, window):
        # initializes public attribute view which is a StartView object
        # uses window from app and image from StartView
        self.view = StartView()
        self._window = window
        self.img = self.view.image


    def display(self):
        """
        blits start menu text and the sprite "start.png" button from StartView
        """
        background = self.view.show_background_image()
        self._window.blit(background, (0, 0))
        menu = self.view.show_start_menu()
        self._window.blit(menu, (50, 50))
        self._window.blit(self.img, self.view.rect)


    def kill_sprite(self):
        """
        kills the sprite (start button in start view)
        """
        self.view.update()
        
