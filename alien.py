import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        # Share the screen it needs to appear on 
        self.screen = ai_game.screen

        # Load the alien image 
        self.image = pygame.image.load("C:/Users/Shivam/AppData/Local/Programs/Microsoft VS Code/alien_spaceship.bmp")
                                        

        # get the rect of the image 
        self.rect = self.image.get_rect()

        # Putting the alien at certain position 
        self.rect.x = self.rect.width # 50
        self.rect.y = self.rect.height # 40

        # Store the alien position 
        self.x = float(self.rect.x)

        # Get the settings 
        self.settings = ai_game.settings

    def update(self):
        # move the alien 
        self.x += self.settings.alien_speed * self.settings.fleet_direction

        # draw the alien on the screen 
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        # Get the screen's rectangle
        screen_rect = self.screen.get_rect()

        # Check if the image is at the screen's right edge  
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)
    