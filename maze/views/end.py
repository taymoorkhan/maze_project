# views/end.py
# End class view page

# import necessary pygame tools 
import pygame
import pygame.locals


class EndView(pygame.sprite.Sprite):

    def __init__(self ):

        """
        Creates a sprite class (button) and text direction that tells the user to start the game

        """

        # use sprite constructor to create sprite
        super().__init__()

        # use a start button image as a button and scales the image
        image = pygame.image.load('views/images/end.png' )
        self.image = pygame.transform.scale(image, (200, 100))

        # creates shortcut attribute for getting the image button location
        self.rect = self.image.get_rect()

        # positions the button on the window
        self.rect.x = 300
        self.rect.y = 300

    def create_text_win(self, display_text):
        """
        creates a text surface for win condition with text direction on how end the game written on it

        :param display_text: string to be displayed on page
        :type display_text: str
        """

        # runs a sysfont pygame function to write text on the page
        impact = pygame.font.SysFont('impact', 50)
        text_surface = impact.render(display_text, True, (107, 140, 255))

        return text_surface

    def create_text_lose(self, display_text):
        """
        creates a text surface for lose condition

        :param display_text: string to be displayed on page
        :type display_text: str
        """
        # runs a sysfont pygame function to write text on the page
        impact = pygame.font.SysFont('impact', 80)
        text_surface = impact.render(display_text, True, (107, 140, 255))

        return text_surface

    def show_end_menu(self, win_loss, score):
        """
        creates text to be displayed using the create_text_surface method and returns the surface to endcontroller

        :param win_loss: True comes in if win, else False
        :type win_loss: bool
        """
        # displays text depending on win or loss
        if win_loss == True:
            display_text = f"You have won with a score of {score}!"
            surface = self.create_text_win(display_text)


        else:
            display_text = "You lose. Game Over."
            surface = self.create_text_lose(display_text)

        return surface

    def show_end_background(self, win_loss):
        """
        creates a background to be displayed depending on condition

        :param win_loss: True comes in if win, else False
        :type win_loss: bool
        """
        if win_loss == True:
            background_img = pygame.image.load("views/images/win.jpg").convert()
            background = pygame.transform.scale(background_img, (800, 800))

        else:
            background_img = pygame.image.load("views/images/lose.jpg").convert()
            background = pygame.transform.scale(background_img, (800, 800))
        return background
