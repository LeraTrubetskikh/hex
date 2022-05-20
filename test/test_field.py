import unittest

from game.field import Field


class FieldTestCase(unittest.TestCase):
    def test_create_field(self):
        field = Field(6)
        self.assertEqual(36, len(field.cells))

    def test_fill_cell(self):
        field = Field(6)
        field.fill_cell((550, 30), 'color')
        self.assertEqual('color', field.cells[0].color)

    def test_fill_cell_by_index(self):
        field = Field(6)
        field.fill_cell_by_index(0, 'color')
        self.assertEqual('color', field.cells[0].color)


if __name__ == '__main__':
    unittest.main()
