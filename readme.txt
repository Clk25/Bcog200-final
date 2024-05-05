Sudoku Solver
Overview
Sudoku Solver is a Python application that provides an easy-to-use graphical interface for inputting Sudoku puzzles and quickly solving them. The application uses a backtracking algorithm to determine the solution to the entered Sudoku puzzle or if the puzzle is invalid indicates if the puzzle is unsolvable. This tool is perfect for both Sudoku enthusiasts who want to check their solutions and those learning how to solve Sudoku puzzles effectively, or perhaps even those who enjoy making puzzles and want to ensure validity before releasing it.

Features
Graphical User Interface: Simple and interactive, allowing for easy input of Sudoku puzzles.
Immediate Feedback: Instantly verifies the validity of the puzzle and provides solutions or error messages.
Backtracking Algorithm: Employs a powerful solving technique to handle even the most challenging puzzles.
Installation
To run Sudoku Solver, you need Python installed on your system along with the tkinter module, which is typically included with standard Python installations. Download the project files to your local machine, navigate to the directory containing the files, and run:
"sudoku_solver.py"

Usage Instructions
Starting the Application: Run the script as outlined above. Initially, an instructions window will appear explaining how to use the application.
NOTE: On certain systems the program will not be executed by merely typing in the script name in the command prompt when in the correct directory, in this case simply input " .\sudoku_solver.py" and the script should run.
Inputting the Puzzle: After closing the instructions window by clicking "Ok", the main Sudoku grid will appear. Enter numbers (1-9) into the grid cells for known values, and leave cells blank for unknowns.
Solving the Puzzle: Click the "Solve" button below the grid to attempt to solve the puzzle. The solution will appear in the grid if solvable.
Handling Errors and Invalid Inputs: If the puzzle is unsolvable or invalid inputs are detected, a message box will provide the appropriate feedback.

Functions:

puzzle_validity(puzzle)
Checks if the provided puzzle configuration is valid (no duplicates in rows, columns, or 3x3 subgrids). Returns True if valid, otherwise False.

next_blank(puzzle)
Finds the next empty cell in the puzzle grid. Returns a tuple (row, col) or (None, None) if no empty cells are found.

valid_move(puzzle, guess, row, col)
Validates whether placing the guess (number from 1 to 9) at the specified row and col is valid according to Sudoku rules.

solver(puzzle)
Attempts to solve the Sudoku puzzle using a backtracking approach. Returns True if the puzzle is solved, otherwise False.

display_solution(puzzle)
Updates the GUI to display the solved puzzle.

parse_grid()
Reads the input from the GUI's grid entries and converts it into a list of lists, which represents the puzzle. Handles and notifies invalid inputs.

solve()
Coordinates reading the grid, validating the puzzle, and solving it. It updates the GUI based on the results.

create_grid(app)
Sets up the GUI for inputting the Sudoku puzzle.

show_main_window()
Initializes and shows the main application window after closing the instructions.

show_instructions()
Displays the initial instructions window with guidelines on how to use the application.

Example Use Cases
Solving a Known Puzzle: Input a puzzle from a newspaper or book to check the solution.
Puzzle Validation: Quickly determine if a partially completed puzzle is still solvable.
