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