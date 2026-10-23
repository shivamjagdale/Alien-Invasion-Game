import pygame 
import pygame.font

class Button:

    def __init__(self, ai_game, msg):

        # give it the screen
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect() # get screen's rect 

        # get the buttons width and height 
        self.width, self.height = 200,50

        # Button's and text color 
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)

        # Button's font 
        self.font = pygame.font.SysFont(None, 48)

        # Get the button's rect 
        self.rect = pygame.Rect(0,0,self.width, self.height)

        # Place the button in the middle of the screen
        self.rect.center = self.screen_rect.center 

        # Prepare the text 
        self._prep_msg(msg) # Take play and prepare it so pygame can display it

    def _prep_msg(self, msg):

        # Turn the text into image 
        self.msg_img = self.font.render(msg, True, self.text_color,
                                        self.button_color)

        # Get the text image's rect 
        self.msg_img_rect = self.msg_img.get_rect()

        # Now place the text image on the button 
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # Display the button on the screen 
        self.screen.fill(self.button_color, self.rect)

        # Put the text image on the screen 
        self.screen.blit(self.msg_img, self.msg_img_rect)

