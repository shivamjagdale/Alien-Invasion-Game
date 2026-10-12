import pygame 
import sys 

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()

        # settings 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
               
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:  
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:   
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit() 

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:   
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:    
            self.ship.moving_left = False    

    def _update_screen(self):
        """Update the images on the screen and flip / show the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()