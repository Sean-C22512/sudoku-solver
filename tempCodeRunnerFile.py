import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_valid_puzzle(self):
        puzzle = [0, 0, 4, 0, 5, 0, 0, 0, 0,
                  9, 0, 0, 7, 3, 4, 6, 0, 0,
                  0, 0, 3, 0, 2, 1, 0, 4, 9,
                  0, 3, 5, 0, 9, 0, 4, 8, 0,
                  0, 9, 0, 0, 0, 0, 0, 3, 0,
                  0, 7, 6, 0, 1, 0, 9, 2, 0,
                  3, 1, 0, 9, 7, 0, 2, 0, 0,
                  0, 0, 9, 1, 8, 2, 0, 0, 3,
                  0, 0, 0, 0, 6, 0, 1, 0, 0]
        solution = solve_sudoku(puzzle)
        self.assertIsNotNone(solution)
        print(solution)

    def test_unsolvable_puzzle(self):
        invalid_puzzle = [1] * 81  # All 1s
        self.assertIsNone(solve_sudoku(invalid_puzzle))

    def test_empty_puzzle(self):
        empty_puzzle = [0] * 81
        self.assertIsNotNone(solve_sudoku(empty_puzzle))

    def test_incomplete_puzzle(self):
        incomplete_puzzle = [5, 3, 0, 0, 7, 0, 0, 0, 0] + [0] * 72
        solution = solve_sudoku(incomplete_puzzle)
        self.assertIsNotNone(solution)

    def test_invalid_input(self):
        invalid_puzzle = [1, 2, 3]  # Incorrect size
        self.assertIsNone(solve_sudoku(invalid_puzzle))

    def test_edge_case(self):
        edge_case_puzzle = [9] + [0] * 80
        self.assertIsNotNone(solve_sudoku(edge_case_puzzle))

if __name__ == '__main__':
    unittest.main()
