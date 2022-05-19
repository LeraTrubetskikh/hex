from game.cell import Cell


class Field:
    def __init__(self, size):
        self.cells = []
        self.size = size
        self.create()
        self.visited_cells = []
        self.ai_win = False
        self.player_win = False

    def get_coordinates(self, x_coord, y_coord):
        return [[x_coord, y_coord], [x_coord + 20, y_coord + 10], [x_coord + 20, y_coord + 30],
                [x_coord, y_coord + 40], [x_coord - 20, y_coord + 30], [x_coord - 20, y_coord + 10]]

    def create(self):
        previous = None
        for i in range(self.size):
            for j in range(self.size):
                if j == 0 and i == 0:
                    cell = Cell(self.get_coordinates(550, 5))
                    self.cells.append(cell)
                    previous = cell
                    continue
                if j == 0:
                    cell = Cell(self.get_coordinates(previous.coordinates[2][0], previous.coordinates[2][1]))
                    self.cells.append(cell)
                    previous = cell
                    continue
                coordinates = self.cells[len(self.cells) - 1].coordinates
                cell = Cell(self.get_coordinates(coordinates[4][0], coordinates[4][1]))
                self.cells.append(cell)

    def fill_cell(self, pos, color):
        for cell in self.cells:
            if abs(cell.coordinates[5][0]) < pos[0] < abs(cell.coordinates[5][0] + 40) \
                    and abs(cell.coordinates[5][1]) < pos[1] < abs(cell.coordinates[5][1] + 20):
                if not cell.visited:
                    cell.fill(color)
                    self.visited_cells.append(cell)
                    return True
        return False

    def fill_cell_by_index(self, index, color):
        self.cells[index].fill(color)
        self.visited_cells.append(self.cells[index])

    # def check_win(self):
    #     if len(self.visited_cells) >= self.field.size:
    #         for cell1 in self.players[self.next_move].end_cells[0]:
    #             for cell2 in self.players[self.next_move].end_cells[1]:
    #                 if self.field.cells[cell1] in self.players[self.next_move].visited_cells and \
    #                         self.field.cells[cell2] in self.players[self.next_move].visited_cells:
    #                     if self.get_way(cell1, cell2, 0, []):
    #                         self.game_display = pygame.display.set_mode((1100, 650))
    #                         self.flag_win = True