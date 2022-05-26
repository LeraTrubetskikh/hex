import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class QUI:
    def __init__(self, game_display):
        self.game_display = game_display
        self.font = pygame.font.SysFont('arial', 36)

    def get_coordinates_for_frame(self, cell, indices, shifts):
        """
        returns the coordinates for the frame(triangle coordinates)
        :param cell:
        :param indices:
        :param shifts: shifts for triangle
        """
        return [[cell.coordinates[indices[0]][indices[1]],
                 cell.coordinates[indices[2]][indices[3]]],
                [cell.coordinates[indices[0]][indices[1]] + shifts[0],
                 cell.coordinates[indices[2]][indices[3]] + shifts[1]],
                [cell.coordinates[indices[0]][indices[1]] + shifts[2],
                 cell.coordinates[indices[2]][indices[3]] + shifts[3]]]

    def draw_side(self, field, color, indices, shifts, fr, to, step=1):
        """draws the side of the frame
        :param field: instance of Field class
        :param color: color for side
        """
        for i in range(fr, to, step):
            coordinates = self.get_coordinates_for_frame(field.cells[i], indices, shifts)
            pygame.draw.polygon(self.game_display, color, coordinates)

    def draw_frame(self, field):
        """draws a frame
        :param field: instance of Field class"""
        self.draw_side(field, RED, [0, 0, 0, 1], [0, -20, -20, 10], 1, field.size)
        self.draw_side(field, RED, [1, 0, 1, 1], [0, 20, 20, -10], field.size ** 2 - field.size + 1, field.size ** 2)
        self.draw_side(field, BLUE, [4, 0, 4, 1], [20, 10, 20, 30], field.size - 1, field.size ** 2 - 1, field.size)
        self.draw_side(field, BLUE, [1, 0, 1, 1], [0, 20, 20, 30], 0, field.size ** 2 - field.size, field.size)

    def draw_field(self, field):
        """
        draws a frame
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
