from game.cell import Cell


class Tetragon:
    def __init__(self, size):
        self.cells = []
        self.field_size = size
        self.create()
        self.visited_cells = []
        self.ai_win = False
        self.player_win = False
        self.frame = []
        self.create_frame()

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

    def create_side(self, color, indices, shifts, fr, to, step=1):
        """draws the side of the frame
        :param color: color for side
        """
        for i in range(fr, to, step):
            coordinates = self.get_coordinates_for_frame(self.cells[i], indices, shifts)
            cell = Cell(coordinates)
            cell.fill(color)
            self.frame.append(cell)

    def create_frame(self):
        """draws a frame"""
        pass
        self.create_side('red', [0, 0, 0, 1], [0, -20, -20, 10], 1, self.field_size)
        self.create_side('red', [1, 0, 1, 1], [0, 20, 20, -10], self.field_size ** 2 - self.field_size + 1, self.field_size ** 2)
        self.create_side('blue', [4, 0, 4, 1], [20, 10, 20, 30], self.field_size - 1, self.field_size ** 2 - 1, self.field_size)
        self.create_side('blue', [1, 0, 1, 1], [0, 20, 20, 30], 0, self.field_size ** 2 - self.field_size, self.field_size)

    def get_coordinates(self, x_coord: int, y_coord: int):
        """returns the coordinates of the polygon"""
        return [[x_coord, y_coord], [x_coord + 20, y_coord + 10], [x_coord + 20, y_coord + 30],
                [x_coord, y_coord + 40], [x_coord - 20, y_coord + 30], [x_coord - 20, y_coord + 10]]

    def create(self):
        """creates a cell array"""
        previous = None
        for i in range(self.field_size):
            for j in range(self.field_size):
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

    def fill_cell(self, pos, color: str):
        """fills a cell by coordinates on the screen
        :param pos: cell coordinates on the screen
        :param color: fill color"""
        for cell in self.cells:
            if abs(cell.coordinates[5][0]) < pos[0] < abs(cell.coordinates[5][0] + 40) \
                    and abs(cell.coordinates[5][1]) < pos[1] < abs(cell.coordinates[5][1] + 20):
                if not cell.visited:
                    cell.fill(color)
                    self.visited_cells.append(cell)
                    return True
        return False

    def fill_cell_by_index(self, index: int, color: str):
        """fill cell by index
        :param index: cell index in array
        :param color: fill color"""
        self.cells[index].fill(color)
        self.visited_cells.append(self.cells[index])

    def get_index_by_pos(self, pos):
        for i in range(len(self.cells)):
            if abs(self.cells[i].coordinates[5][0]) < pos[0] < abs(self.cells[i].coordinates[5][0] + 40) \
                    and abs(self.cells[i].coordinates[5][1]) < pos[1] < abs(self.cells[i].coordinates[5][1] + 20):
                return i
        return 0
