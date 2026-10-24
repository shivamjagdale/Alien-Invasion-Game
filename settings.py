class Settings:

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullets 
        self.bullet_speed = 2.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # alien speed
        self.alien_speed = 1.0

        self.alien_points = 50 # Points for destroying an alien 
        
        self.fleet_drop_speed = 10 # how far down should the fleet move?

        self.fleet_direction = 1 # which horizontal direction should the fleet move?

        # How quickly the game speeds up 
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that can change while you play the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.alien_points = 50

        # Start the aliens by moving them to the right 
        self.fleet_direction = 1


    def increase_speed(self):
        """Increase the speed by 10%"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
# main 