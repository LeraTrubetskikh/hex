import pygame

WHITE = (255, 255, 255)

class Button:
    def __init__(self, x, y, size, text, act):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('twcen', size)
        self.text = text
        self.text_surface = self.my_font.render(self.text, True, WHITE)
        self.w = self.text_surface.get_rect()[2]
        self.h = self.text_surface.get_rect()[3]
        self.x = x
        self.y = y
        self.state = 'normal'
        self.action = act

    def check_state(self, position):
        if (abs(self.x) < position[0] < abs(self.x + self.w)
                and abs(self.y) < position[1] < abs(self.y + self.h)):
            self.state = 'highlighted'
        else:
            self.state = 'normal'
