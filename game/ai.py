import random


class AI:
    def __init__(self, field_size):
        self.color = (0, 0, 255)
        self.field_size = field_size
        self.LEFT_RED = [i for i in range(self.field_size)]
        self.LEFT_BLUE = [i for i in range(self.field_size - 1, self.field_size ** 2 - 1, self.field_size)]
        self.RIGHT_RED = [i for i in range(self.field_size ** 2 - self.field_size, self.field_size ** 2)]
        self.RIGHT_BLUE = [i for i in range(0, self.field_size ** 2 - self.field_size, self.field_size)]
        self.graph = []
        self.field = {}
        self.get_graph()

    def get_graph(self):
        with open('../resources/config11x11.txt', 'r') as f:
            for line in f.readlines():
                l = []
                for el in line.split(' '):
                    l.append(int(el))
                self.graph.append(l)

    def wave(self, cell, cur, previous):
        for i in self.graph[cell]:
            if self.field[i][0] != -1 and i != previous:
                if self.field[i][0] > cur:
                    self.field[i] = (cur, cell)
                    self.wave(i, cur + 1, cell)

    def restore_path(self, end, field):
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
        for i in range(field.size ** 2):
            if i == start:
                self.field[start] = (0, -1)
                continue
            if field.cells[i].color == 'red':
                self.field[i] = (-1, -1)
            else:
                self.field[i] = (field.size ** 2 + 1, -1)
        self.wave(start, 1, -1)
        if self.field[end] != (field.size ** 2 + 1, -1):
            return self.restore_path(end, field)
        else:
            return None

    def move(self, field):
        min = field.size ** 2
        min_computer_path = []
        for start in self.RIGHT_BLUE:
            if field.cells[start].color == 'red':
                continue
            for end in self.LEFT_BLUE:
                if field.cells[end].color == 'red':
                    continue
                path = self.get_path(start, end, field)
                if path is not None:
                    if len(path) < min:
                        min_computer_path = path
                        min = len(path)
        if min == 0:
            field.ai_win = True
        elif min == field.size ** 2:
            field.player_win = True
        else:
            field.fill_cell_by_index(min_computer_path[0], 'blue')
