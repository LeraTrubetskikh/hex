import random
import sys

import pygame as pygame

from game.ai import AI
from game.button import Button
from game.gui import QUI
from game.hexagon import Hexagon
from game.square import Square
from game.tetragon import Tetragon


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1100, 650))
        self.field = Tetragon(11)
        self.ai = AI(11, 'config11x11.txt', [], [], [], [])
        self.ai_move = False
        i = random.choice([1, 2])
        if i == 1:
            self.ai_move = True
        self.gui = QUI(self.game_display)
        self.game_started = False
        self.buttons = [Button(420, 200, 50, 'Шестиугольник', lambda: self.create_hexagon()),
                        Button(420, 255, 50, 'Ромб', lambda: self.create_tetragon())]

    def main_menu(self):
        while True:
            self.gui.update_menu(self.buttons)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                for button in self.buttons:
                    button.check_state(pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.buttons:
                            if abs(button.x) < pos[0] < abs(button.x + button.w) \
                                    and abs(button.y) < pos[1] < abs(button.y + button.h):
                                button.state = 'pressed'
                                self.game_display = pygame.display.set_mode((1100, 650))
                                pygame.display.flip()
                                return button
            pygame.display.flip()

    def create_hexagon(self):
        self.field = Hexagon(6)
        left_red = [0, 1, 2, 3, 4, 5, 6, 13, 21]
        left_blue = [5, 12, 20, 29, 39, 50, 60, 69, 77]
        right_red = [77, 84, 85, 86, 87, 88, 89, 90]
        right_blue = [21, 30, 40, 51, 61, 70, 78, 85]
        self.ai = AI(6, 'config6x6.txt', left_red, left_blue, right_red, right_blue)

    def create_tetragon(self):
        self.field = Tetragon(11)
        left_red = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        left_blue = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 120]
        right_red = [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
        right_blue = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
        self.ai = AI(11, 'config11x11.txt', left_red, left_blue, right_red, right_blue)

    def start(self):
        """updates game's state and draws it on the screen"""
        self.main_menu().action()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.field.fill_cell(pos, 'red'):
                        self.ai_move = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_display.fill((30, 30, 30))
                        self.main_menu().action()
            self.game_display.fill((30, 30, 30))
            self.gui.update(self.field)
            if self.ai_move:
                self.ai.move(self.field)
                self.gui.update(self.field)
                pygame.display.update()
                self.ai_move = False
            pygame.display.flip()
            pygame.time.delay(20)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.start()
