import random


class AI:
    def __init__(self):
        self.color = (0, 0, 255)
        self.LEFT_RED = [0, 1, 2, 3, 4, 5]
        self.LEFT_BLUE = [5, 11, 17, 23, 29, 35]
        self.RIGHT_RED = [30, 31, 32, 33, 34, 35]
        self.RIGHT_BLUE = [0, 6, 12, 18, 24, 30]


    # def get_path(self, isAI, cell):
    #     if isAI:

    def move(self, field):
        i = random.randint(0, field.size ** 2 - 1)
        while field.cells[i].visited:
            i = random.randint(0, field.size ** 2 - 1)
        field.fill_cell_by_index(i, 'blue')
        # min_score = 121
        # min_computer_path = []
        # for cell in self.LEFT_BLUE:
        #     computer_path = self.get_path(True)
        #     player_path = self.get_path(False)
        #     if len(player_path) - len(computer_path) < min_score:
        #         min_computer_path = computer_path
        # for cell in self.RIGHT_BLUE:
        #     computer_path = self.get_path(True)
        #     player_path = self.get_path(False)
        #     if len(player_path) - len(computer_path) < min_score:
        #         min_computer_path = computer_path
        # field.fill_cell(field.cells[min_computer_path[0]])


