import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class QUI:
    def __init__(self, game_display):
        self.game_display = game_display
        self.font = pygame.font.SysFont('arial', 36)

    def draw_frame(self, field):
        """draws a frame
        :param field: instance of Field class"""
        for cell in field.frame:
            if cell.color == 'red':
                pygame.draw.polygon(self.game_display, RED, cell.coordinates)
            if cell.color == 'blue':
                pygame.draw.polygon(self.game_display, BLUE, cell.coordinates)

    def draw_field(self, field):
        """draws a field
        :param field: instance of Field class
        """
        for cell in field.cells:
            if cell.visited:
                if cell.color == 'red':
                    pygame.draw.polygon(self.game_display, RED, cell.coordinates)
                if cell.color == 'blue':
                    pygame.draw.polygon(self.game_display, BLUE, cell.coordinates)
            pygame.draw.polygon(self.game_display, WHITE, cell.coordinates, 2)

    def print_message(self, message: str, pos):
        """prints a message on the screen
        :param message: message text
        :param pos: position of the text on the screen
        """
        surf = self.font.render(message, False, WHITE)
        rect = surf.get_rect(center=pos)
        self.game_display.blit(surf, rect)

    def update(self, field):
        """
        draws the current state of all game objects
        :param field: instance of Field class
        """
        if field.player_win:
            self.print_message('You win', (550, 300))
        elif field.ai_win:
            self.print_message('You lose', (550, 300))
        else:
            self.draw_frame(field)
            self.draw_field(field)

    def update_menu(self, buttons):
        for button in buttons:
            if button.state == 'normal':
                text_surface = self.font.render(button.text, True, WHITE)
                self.game_display.blit(text_surface, (button.x, button.y))
            elif button.state == 'highlighted':
                text_surface = self.font.render(button.text, True, RED)
                self.game_display.blit(text_surface, (button.x, button.y))
