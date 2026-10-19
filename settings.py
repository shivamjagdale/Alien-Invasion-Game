class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 5

        # bullets 
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # alien speed
        self.alien_speed = 1.0
        
        self.fleet_drop_speed = 10 # how far down should the fleet move?

        self.fleet_direction = 1 # which horizontal direction should the fleet move?
        

# main 