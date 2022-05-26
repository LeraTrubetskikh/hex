import unittest

from game.ai import AI
from game.field import Field


class AITestCase(unittest.TestCase):
    def test_create_graph(self):
        ai = AI(11, 'config11x11.txt')
        self.assertEqual(121, len(ai.graph))

    def test_find_min_path_on_empty_field(self):
        ai = AI(11, 'config11x11.txt')
        field = Field(11)
        path = ai.get_path(0, 10, field)
        expected_path = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(expected_path, path)

    def test_find_min_path_on_filled_field(self):
        ai = AI(11, 'config11x11.txt')
        field = Field(11)
        for i in range(121):
            field.fill_cell_by_index(i, 'red')
        path = ai.get_path(0, 10, field)
        expected_path = None
        self.assertEqual(expected_path, path)

    def test_find_min_path_on_lose_field(self):
        ai = AI(11, 'config11x11.txt')
        field = Field(11)
        for i in [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 111]:
            field.fill_cell_by_index(i, 'red')
        path = ai.get_path(0, 10, field)
        expected_path = None
        self.assertEqual(expected_path, path)


if __name__ == '__main__':
    unittest.main()
