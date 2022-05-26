import unittest

from game.cell import Cell


class CellTestCase(unittest.TestCase):
    def create_cell(self):
        cell = Cell((0, 0))
        self.assertFalse(cell.visited)
        self.assertEqual('white', cell.color)
        self.assertEqual((0, 0), cell.color)


    def test_fill_cell(self):
        cell = Cell((0, 0))
        cell.fill('color')
        self.assertEqual('color', cell.color)
        self.assertEqual((0, 0), cell.coordinates)

    def test_visited_cell(self):
        cell = Cell((0, 0))
        cell.fill('color')
        self.assertTrue(cell.visited)


if __name__ == '__main__':
    unittest.main()
