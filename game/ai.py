import random


class AI:
    def __init__(self, field_size: int, config: str, lr, lb, rr, rb):
        self.color = (0, 0, 255)
        self.field_size = field_size
        self.LEFT_RED = lr
        self.LEFT_BLUE = lb
        self.RIGHT_RED = rr
        self.RIGHT_BLUE = rb
        self.graph = []
        self.get_graph(config)
        self.field = {}
        self.last_cell = -1

    def get_graph(self, file_name):
        """defines a graph using link lists from a file"""
        with open('../resources/{0}'.format(file_name), 'r') as f:
            for line in f.readlines():
                spl = []
                for el in line.split(' '):
                    spl.append(int(el))
                self.graph.append(spl)

    def wave(self, cell: int, cur: int, previous: int):
        """wave algorithm for finding the shortest path
        :param cell: start cell
        :param cur: wave number
        :param previous: previous cell"""
        for i in self.graph[cell]:
            if self.field[i][0] != -1 and i != previous:
                if self.field[i][0] > cur:
                    self.field[i] = (cur, cell)
                    self.wave(i, cur + 1, cell)

    def restore_path(self, end: int, field):
        """restores the path
        :param end: last node of the path
        :param field: instance of Field class"""
        cell = self.field[end]
        path = []
        if field.cells[end].color != 'blue':
            path.append(end)
        while cell[0] != 0:
            if field.cells[cell[1]].color != 'blue':
                path.append(cell[1])
            cell = self.field[cell[1]]
        return path

    def get_path(self, start, end, field):
        self.field = {}
        for i in range(len(field.cells)):
            if i == start:
                self.field[start] = (0, -1)
                continue
            if field.cells[i].color == 'red':
                self.field[i] = (-1, -1)
            else:
                self.field[i] = (len(field.cells) + 1, -1)
        self.wave(start, 1, -1)
        if self.field[end] != (len(field.cells) + 1, -1) and self.field[end] != (-1, -1):
            return self.restore_path(end, field)

    def first_move(self, field):
        if field.visited_cells:
            pos = field.visited_cells[0].coordinates[0]
            index = field.get_index_by_pos((pos[0], pos[1] + 15))
            if index in self.LEFT_RED:
                self.last_cell = random.choice(self.LEFT_BLUE[-3: -1])
            elif index in self.RIGHT_RED:
                self.last_cell = random.choice(self.LEFT_BLUE[0: 2])
            else:
                self.last_cell = random.choice(self.LEFT_BLUE)
            field.fill_cell_by_index(self.last_cell, 'blue')
        else:
            self.last_cell = random.choice(self.LEFT_BLUE)
            field.fill_cell_by_index(self.last_cell, 'blue')

    def move(self, field):
        if self.last_cell == -1:
            self.first_move(field)
        else:
            min = len(field.cells)
            min_computer_path = []
            for end in self.RIGHT_BLUE:
                if field.cells[end].color == 'red':
                    continue
                path = self.get_path(self.last_cell, end, field)
                if path is not None:
                    if len(path) < min:
                        min_computer_path = path
                        min = len(path)
            if min == 0:
                field.ai_win = True
            elif min == len(field.cells):
                field.player_win = True
            else:
                self.last_cell = min_computer_path[len(min_computer_path) - 1]
                field.fill_cell_by_index(self.last_cell, 'blue')

# todo форма(несколько фигур)
# усовершенсвовать алгоритм(учитывать первй ход игрока)
# первым ходит ирок или комп (рандом)