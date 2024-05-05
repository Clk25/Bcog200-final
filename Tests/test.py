import pytest
import sys
import os

# Add the directory containing sudoku_solver.py to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sudoku_solver import puzzle_validity, next_blank, valid_move

def test_puzzle_validity():
    # Test a valid and an invalid Sudoku configuration
    valid_puzzle = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]
    invalid_puzzle = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 5],  # Error here, 5 repeated in last column
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]
    valid_result = puzzle_validity(valid_puzzle)
    invalid_result = puzzle_validity(invalid_puzzle)
    print("Validity of valid puzzle:", valid_result)  # Should print True
    print("Validity of invalid puzzle:", invalid_result)  # Should print False

def test_next_blank():
    # Test finding the next empty cell
    puzzle_with_empty = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [-1, 4, 5, 2, 8, 6, 1, 7, 9]  # Last row, first cell is empty
    ]
    next_empty = next_blank(puzzle_with_empty)
    print("Next empty cell:", next_empty)  # Should print (8, 0)

def test_valid_move():
    # Test a valid move
    puzzle = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [-1, 4, 5, 2, 8, 6, 1, 7, 9]  # Last row, first cell is empty
    ]
    move_validity = valid_move(puzzle, 3, 8, 0)
    print("Is move valid (3 at (8,0)):", move_validity)  # Should print True

def main():
    test_puzzle_validity()
    test_next_blank()
    test_valid_move()

if __name__ == "__main__":
    main()
