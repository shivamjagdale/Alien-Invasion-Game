import pygame 
import pygame.font 

class Scoreboard:
    """A class to report storing information"""

    def __init__(self, ai_game):
        # Share the screen 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect() # Get the screen's rect 

        # Import the settings
        self.settings = ai_game.settings 

        # Import game_stats
        self.stats = ai_game.stats

        # Choose the text color and font 
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prep the score 
        self.prep_score()

        # Prep the high score 
        self.prep_high_score()

        # prep the game level 
        self.prep_level()

    def prep_score(self):
        """Turn the score into rendered image"""

        rounded_score = round(self.stats.score, -1)
    
        score_str = f"{rounded_score:,}" # 100
        self.score_img = self.font.render(score_str,True, 
                                        self.text_color, 
                                        self.settings.bg_color)
        
        # Rect for score image 
        self.score_img_rect = self.score_img.get_rect()

        # Position the score 
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def prep_high_score(self):
        """Turn high score into rendered image"""
        self.high_score_round = round(self.stats.high_score, -1)
        self.high_score_str = f"{self.high_score_round:,}"

        # Turn high score into image 
        self.high_score_img = self.font.render(self.high_score_str, True, 
                                               self.text_color, 
                                               self.settings.bg_color)

        # Get the high score's rect 
        self.high_score_rect = self.high_score_img.get_rect()

        # Place the high score on the screen 
        self.high_score_rect.centerx = self.screen_rect.centerx  
        self.high_score_rect.top = self.score_img_rect.top

    def check_high_score(self):
        """Did the player just beat their previous high score?"""

        # compare scores 
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score # update the high score
            self.prep_high_score() # update the image 


    def prep_level(self):
        self.prep_level_str = f"{self.stats.level:,}"

        # Prep level into img 
        self.prep_level_img = self.font.render(self.prep_level_str,
                                               True, self.text_color,
                                               self.settings.bg_color)

        # Get the prep level img's rect 
        self.prep_level_rect = self.prep_level_img.get_rect()

        # Decide where to place the prep level img
        self.prep_level_rect.right = self.score_img_rect.right
        self.prep_level_rect.top = self.score_img_rect.bottom + 10

    def show_score(self):
        # Score
        self.screen.blit(self.score_img, self.score_img_rect)

        # High score 
        self.screen.blit(self.high_score_img, self.high_score_rect)

        # Game level 
        self.screen.blit(self.prep_level_img, self.prep_level_rect)