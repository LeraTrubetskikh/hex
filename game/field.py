from game.cell import Cell


class Field:
    def __init__(self, size):
        self.cells = []
        self.size = size
        self.create()
        self.visited_cells = []

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
        self.fill_cell((self.cells[index].coordinates[0][0] + 1, self.cells[index].coordinates[0][1] - 1), color)
