import pygame 
import sys 

from settings import Settings
from ship import Ship
from bullet import Bullet

from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()

        # settings 
        self.settings = Settings()

        # create the bullet group
        self.bullets = pygame.sprite.Group() # [       ] group

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion LOL")

        # frame rate
        self.clock = pygame.time.Clock()

        # background color 
        self.bg_color = (200, 200, 200)

        # ship                
        self.ship = Ship(self)

        # Aliens                           
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_aliens(current_x, current_y)
                current_x += 2* alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_aliens(self,x_pos, y_pos):
        new_alien = Alien(self)
        new_alien.x = x_pos # 96
        new_alien.rect.x = x_pos # 96
        new_alien.rect.y = y_pos 
        self.aliens.add(new_alien)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:   
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) # creating new bullet "object"
            self.bullets.add(new_bullet) # Then add that newly created bullet to the group

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:   
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:    
            self.ship.moving_left = False 


    def _update_screen(self):
        """Update the images on the screen and flip / show the new screen"""
        self.screen.fill(self.settings.bg_color)

        # draw the bullet 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
             
        self.ship.blitme()

        # draw aliens                
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

    def _update_bullets(self):
            """Update position of bullets and get rid of old bullets."""
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.bullet_rect.bottom <=0:
                    self.bullets.remove(bullet)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """check if the fleet has reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # we want to change the fleets direction once so it's outside the for loop

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

# main