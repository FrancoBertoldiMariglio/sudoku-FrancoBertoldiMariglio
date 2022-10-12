from sudokuException import ExpectionSetNumberRowColumn
from sudokuException import ExpectionSetNumberMatrix


class Sudoku():

    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def setNumber(self, row, column, number):
        for i in range(9):
            if self.board[row][i] == number:
                raise ExpectionSetNumberRowColumn

        for i in range(9):
            if self.board[i][column] == number:
                raise ExpectionSetNumberRowColumn

        listaIterable = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for range1 in listaIterable:
            for range2 in listaIterable:
                for x in range1:
                    for y in range2:
                        if self.board[x][y] == number:
                            raise ExpectionSetNumberMatrix

        self.board[row][column] = number
