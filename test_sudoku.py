import unittest
from sudokuException import ExpectionSetNumberRowColumn
from sudokuException import ExpectionSetNumberMatrix
from sudoku import Sudoku
from parameterized import parameterized


class TestSudoku(unittest.TestCase):

    def test_create_board(self):
        sudoku = Sudoku()
        self.assertEqual(len(sudoku.board), 9)
        self.assertEqual(len(sudoku.board[0]), 9)

    def test_set_number_basic(self):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)

    @parameterized.expand([(2, 1), (1, 2)])
    def test_set_number_validate_column(self, a, b):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        with self.assertRaises(ExpectionSetNumberRowColumn):
            sudoku.setNumber(a, b, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[a][b], 0)

    """ def test_set_number_validate_column(self):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        with self.assertRaises(ExpectionSetNumberRowColumn):
            sudoku.setNumber(2, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[2][1], 0)

    def test_set_number_validate_row(self):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        with self.assertRaises(ExpectionSetNumberRowColumn):
            sudoku.setNumber(1, 2, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[1][2], 0) """

    @parameterized.expand([

        (1, 1, 9, 2, 2, 9, 0),
        (0, 0, 9, 2, 1, 9, 0),
        (0, 0, 9, 2, 2, 9, 0),
        (6, 6, 9, 8, 8, 9, 0),
        (6, 6, 9, 8, 7, 9, 0),
        (0, 6, 9, 1, 7, 9, 0),
        (6, 0, 9, 7, 1, 9, 0),
        (6, 3, 9, 7, 4, 9, 0),
        (6, 3, 9, 8, 4, 9, 0),   
        ])
    def test_set_number_validate_matrix(self, a, b, c, d, e, f, g):
        sudoku = Sudoku()
        sudoku.setNumber(a, b, c)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(d, e, f)
        self.assertEqual(sudoku.board[a][b], f)
        self.assertEqual(sudoku.board[d][e], g)


if __name__ == '__main__':
    unittest.main()
