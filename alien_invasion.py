import pygame 
import sys 

from time import sleep 

from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button

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

        # Import game stats
        self.stats = GameStats(self)

        # Game active variable
        self.game_active = False

        # Create the play button 
        self.play_button = Button(self, "Play")

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            # If the alien hit our ship then -1
            self.stats.ships_left -=1

            # Remove aliens and remove bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship 
            self._create_fleet()
            self.ship.center_ship()

            # pause the game
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =  pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.game_active = True 

            # Remove aliens and bullets 
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and then center the ship
            self._create_fleet()
            self.ship.center_ship()

            # hide the mouse 
            pygame.mouse.set_visible(False)

                
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

        # Draw the play button 
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullets(self):
            """Update position of bullets and get rid of old bullets."""
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)
            self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
            """Respond to bullet alien collisions"""
            """Check for any bullets that have hit aliens."""
            """If so get rid of the bullet and the alien"""
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

            # Repopulate the entire fleet and destroy remaining bullets
            if not self.aliens:
                self.bullets.empty()
                self._create_fleet()


    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Did any alien hit our ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if the aliens reached the bottom of the screen 
        self._check_aliens_reached_bottom()

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


    def _check_aliens_reached_bottom(self):
        """check weather an alien has reached the bottom"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this same as if a ship got hit 
                self._ship_hit()
                break 


    def run_game(self):

        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

# main