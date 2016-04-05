#!/usr/bin/env python3
# SUDOKU SOLVER

# Project   Solve sudoku games
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      04.04.2016
# Python    3.5.1

field = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]


class Sudoku:

    def __init__(self, game):
        self.game = game

    @staticmethod
    def which_range(row_col_id):
        """ (int) -> list
        Based on given row_id or col_id return the range of the 3x3 box.
        """

        if row_col_id < 3:
            return [0, 1, 2]
        elif 3 <= row_col_id < 6:
            return [3, 4, 5]
        elif 6 <= row_col_id:
            return [6, 7, 8]

    def solve(self):
        """
        Solve the Suduko game stored in self.game variable.
        """
        solved = True
        n = 9
        for row_id in range(n):
            for col_id in range(n):
                val = self.game[row_id][col_id]
                if val == 0:
                    solved = False
                    feas = []
                    row = self.game[row_id]
                    col = [self.game[r][col_id] for r in range(0,9)]
                    row_range = self.which_range(row_id)
                    col_range = self.which_range(col_id)
                    box = [self.game[r][c] for c in col_range for r in row_range]
                    for x in range(1,10):
                        if (x not in row) and (x not in col) and (x not in box):
                            feas.append(x)
                    if len(feas) == 1:
                        self.game[row_id][col_id] = feas[0]

        # Recursive until solved
        if solved == False:
            self.solve()
        else:
            self.printing()

    def display(self):
        """
        Print out the stored Sudoku game.
        """
        n = 9    # num of rows and cols
        s = 3    # separator after s num of chars
        l = '- - - + - - - + - - -'

        # iterate over rows
        for row_id in range(n):
            if row_id > 0: print()
            if row_id % s == 0 and row_id > 0: print(l)

            # iterate over cols
            for col_id in range(n):
                e = ' '
                if (col_id + 1) % s == 0 and 0 < col_id < (n - 1):
                    e = ' | '

                # print current value
                val = self.game[row_id][col_id]
                val = val if val != 0 else '.'
                print(val, end=e)
