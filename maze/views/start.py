#views/start.py
#Start class view page

# import necessary pygame tools 
import pygame
import pygame.locals

class StartView(pygame.sprite.Sprite):

    """
    Creates a sprite class (button) and text direction that tells the user to start the game

    """

    def __init__(self):
        # use sprite constructor to create sprite
        super().__init__()
        # use a start button image as a button and scales the image
        image = pygame.image.load('views/images/start.png')
        self.image = pygame.transform.scale(image, (260, 200))
        # creates shortcut attribute for getting the image button location
        self.rect = self.image.get_rect()

        # positions the button on the window
        self.rect.x = 500
        self.rect.y = 250

    def create_text_surface(self, display_text):
        """
        creates a text surface with text direction on how to start the game written on it

        :param display_text: string to be displayed on page
        :type display_text: str
        """

        # runs a sysfont pygame function to write text on the page
        impact = pygame.font.SysFont('impact', 80)
        text_surface = impact.render(display_text, True, (240, 106, 17))

        return text_surface


    def show_start_menu(self):
        """
        creates text to be displayed using the create_text_surface method and returns the surface to startcontroller

        """
        display_text = "Kidd World: The Maze"
        surface = self.create_text_surface(display_text)
        return surface


    def show_background_image(self):
        """
        creates the background image for the start menu and returns the background to the startcontroller
        """
        background_img = pygame.image.load("views/images/alexthekidd.jpg").convert()
        background = pygame.transform.scale(background_img, (800, 800))
        return background

    def update(self):
        """
        kills sprite
        """
        self.kill()
