import sys

import pygame as pygame

from game.ai import AI
from game.field import Field
from game.gui import QUI


def start():
    pygame.init()
    game_display = pygame.display.set_mode((1100, 650))
    field = Field(11)
    ai = AI(11)
    ai_move = False
    gui = QUI(game_display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if field.fill_cell(pos, 'red'):
                    ai_move = True
        game_display.fill((30, 30, 30))
        gui.update(field)
        if ai_move:
            pygame.display.update()
            ai.move(field)
            ai_move = False
            gui.update(field)
        pygame.display.flip()
        pygame.time.delay(20)
        pygame.display.update()


if __name__ == "__main__":
    start()




