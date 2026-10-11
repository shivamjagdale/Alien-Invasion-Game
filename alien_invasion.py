import pygame 
import sys 

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()

        # settings 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion LOL")

        # frame rate
        self.clock = pygame.time.Clock()

        # background color 
        self.bg_color = (200, 200, 200)

        # ship
        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update the images on the screen and flip / show the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()