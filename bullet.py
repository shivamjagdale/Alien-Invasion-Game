import pygame 
from pygame.sprite import Sprite 

from settings import Settings
from ship import Ship

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # import settings 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # import ship 
        self.ship = ai_game.ship

        # bullet's rect 
        self.rect = pygame.Rect(0,0, 
                                       self.settings.bullet_width, 
                                       self.settings.bullet_height)

        # place the bullet on the top of the ship
        self.rect.midtop = self.ship.rect.midtop

        # store the bullet's starting position
        self.y = float(self.rect.y) 

    def update(self):
        # make ships bullet go upwards
        self.y -=  self.settings.bullet_speed 

        # and make the bullet appear on screen 
        self.rect.y = self.y 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

# main