import unittest
from sudokuException import ExpectionSetNumberRowColumn
from sudokuException import ExpectionSetNumberMatrix
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_create_board(self):
        sudoku = Sudoku()
        self.assertEqual(len(sudoku.board), 9)
        self.assertEqual(len(sudoku.board[0]), 9)

    def test_set_number_basic(self):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)

    def test_set_number_validate_column(self):
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
        self.assertEqual(sudoku.board[1][2], 0)

    def test_set_number_validate_matrix(self):
        sudoku = Sudoku()
        sudoku.setNumber(1, 1, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(2, 2, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[2][2], 0)

    def test_set_number_validate_matrix1(self):
        sudoku = Sudoku()
        sudoku.setNumber(0, 0, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(2, 1, 9)
        self.assertEqual(sudoku.board[0][0], 9)
        self.assertEqual(sudoku.board[2][1], 0)

    def test_set_number_validate_matrix2(self):
        sudoku = Sudoku()
        sudoku.setNumber(0, 0, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(2, 2, 9)
        self.assertEqual(sudoku.board[0][0], 9)
        self.assertEqual(sudoku.board[2][2], 0)

    def test_set_number_validate_matrix3(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 6, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(8, 8, 9)
        self.assertEqual(sudoku.board[6][6], 9)
        self.assertEqual(sudoku.board[8][8], 0)

    def test_set_number_validate_matrix4(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 6, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(8, 7, 9)
        self.assertEqual(sudoku.board[6][6], 9)
        self.assertEqual(sudoku.board[8][7], 0)

    def test_set_number_validate_matrix5(self):
        sudoku = Sudoku()
        sudoku.setNumber(0, 6, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(1, 7, 9)
        self.assertEqual(sudoku.board[0][6], 9)
        self.assertEqual(sudoku.board[1][7], 0)

    def test_set_number_validate_matrix6(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 0, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(7, 1, 9)
        self.assertEqual(sudoku.board[6][0], 9)
        self.assertEqual(sudoku.board[7][1], 0)

    def test_set_number_validate_matrix7(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 0, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(7, 1, 9)
        self.assertEqual(sudoku.board[6][0], 9)
        self.assertEqual(sudoku.board[7][1], 0)

    def test_set_number_validate_matrix7(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 3, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(7, 4, 9)
        self.assertEqual(sudoku.board[6][3], 9)
        self.assertEqual(sudoku.board[7][4], 0)

    def test_set_number_validate_matrix8(self):
        sudoku = Sudoku()
        sudoku.setNumber(6, 3, 9)
        with self.assertRaises(ExpectionSetNumberMatrix):
            sudoku.setNumber(8, 4, 9)
        self.assertEqual(sudoku.board[6][3], 9)
        self.assertEqual(sudoku.board[8][4], 0)


if __name__ == '__main__':
    unittest.main()