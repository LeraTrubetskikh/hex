class Cell:
    def __init__(self, coordinates):
        self.visited = False
        self.color = 'white'
        self.coordinates = coordinates

    def fill(self, color: str):
        """fill cell
        :param color: fill color"""
        self.visited = True
        self.color = color
