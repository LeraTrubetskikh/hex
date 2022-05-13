class Cell:
    def __init__(self, coordinates):
        self.visited = False
        self.color = 'white'
        self.coordinates = coordinates

    def fill(self, color):
        self.visited = True
        self.color = color
