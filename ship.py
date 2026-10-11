import pygame
import os 

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        # load the image 
        self.image = pygame.image.load("C:/Users/Shivam/AppData/Local/Programs/Microsoft VS Code/DurrrSpaceShip.bmp")
        self.image_rect = self.image.get_rect() # get it's rect 

        # put the ship at the bottom of the screen
        self.image_rect.midbottom = self.screen_rect.midbottom 

    # draw the ship on screen 
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)