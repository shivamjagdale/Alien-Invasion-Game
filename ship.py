import pygame
import os 
from settings import Settings

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        # import settings 
        self.settings = Settings()

        # load the image 
        self.image = pygame.image.load("C:/Users/Shivam/AppData/Local/Programs/Microsoft VS Code/DurrrSpaceShip.bmp")
        self.image_rect = self.image.get_rect() # get it's rect 

        # put the ship at the bottom of the screen
        self.image_rect.midbottom = self.screen_rect.midbottom 
        
        # moving right 
        self.moving_right = False 

        # moving left
        self.moving_left = False 

        # Get the ship position exactly 
        self.x = float(self.image_rect.x)

    def update(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.image_rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.image_rect.x = self.x 
        
    # draw the ship on screen 
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

# main