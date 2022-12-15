import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
class Menu: 
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2
    def __init__(self, message, screen):

        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True,(0,0,0))
        self.text2 = self.font.render(message, True,(255,255,255))
        self.text3 = self.font.render(message, True,(255,255,255))
        self.text4 = self.font.render(message, True,(255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect2 = self.text2.get_rect()
        self.text_rect3 = self.text3.get_rect()
        self.text_rect4 = self.text4.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        self.text_rect2.center = (self.half_screen_width, self.half_screen_height + 50)
        self.text_rect3.center = (self.half_screen_width, self.half_screen_height + 100)
        self.text_rect4.center = (self.half_screen_width, self.half_screen_height + 150)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text_rect2)
        screen.blit(self.text3, self.text_rect3)
        screen.blit(self.text4, self.text_rect4)
        

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run() 

    def reset_screen_color(self, screen): 
        screen.fill((255,255,255))
    
    def update_message(self, message, message2, message3, message4): 
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

        self.text2 = self.font.render(message2, True, (0,0,0))
        self.text_rect2 = self.text.get_rect()
        self.text_rect2.center = (self.half_screen_width, self.half_screen_height + 50)

        self.text3 = self.font.render(message3, True, (0,0,0))
        self.text_rect3 = self.text.get_rect()
        self.text_rect3.center = (self.half_screen_width, self.half_screen_height + 100)

        self.text4 = self.font.render(message4, True, (0,0,0))
        self.text_rect4 = self.text.get_rect()
        self.text_rect4.center = (self.half_screen_width, self.half_screen_height + 150)