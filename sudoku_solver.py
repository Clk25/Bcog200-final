import tkinter as tk
from tkinter import messagebox

def puzzle_validity(puzzle):
    # Check for duplicates in rows, columns, and blocks
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]
            if val != -1:  # Check if the cell is not empty
                if val in rows[r]:
                    return False  # Duplicate in row
                rows[r].add(val)

                if val in columns[c]:
                    return False  # Duplicate in column
                columns[c].add(val)

                block_index = (r // 3) * 3 + (c // 3)
                if val in blocks[block_index]:
                    return False  # Duplicate in block
                blocks[block_index].add(val)

    return True

def next_empty(puzzle):
    # Find an empty space in the puzzle
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def valid_guess(puzzle, guess, row, col):
    # Determines if the guess at the row/col of the puzzle is a valid guess
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # Solve sudoku using backtracking technique
    row, col = next_empty(puzzle)
    if row is None:  # If no empty space is left, puzzle is solved
        return True

    for guess in range(1, 10):
        if valid_guess(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = -1  # Reset guess

    return False  # Trigger backtracking

def display_solution(puzzle):
    # Display the solution on the grid
    for row in range(9):
        for col in range(9):
            grid_entries[row][col].delete(0, tk.END)
            grid_entries[row][col].insert(0, puzzle[row][col])

def parse_grid():
    puzzle = []
    for row in range(9):
        row_vals = []
        for col in range(9):
            val = grid_entries[row][col].get().strip()
            if val.isdigit() and 1 <= int(val) <= 9:
                row_vals.append(int(val))
            elif val == "":
                row_vals.append(-1)
            else:
                # Handle invalid input
                messagebox.showinfo("Input Error", "Invalid input detected. Please enter only numbers from 1 to 9.")
                return None  # Return None to indicate an error in input
        puzzle.append(row_vals)
    return puzzle

def solve():
    puzzle = parse_grid()
    if puzzle is None:
        return  # Exit the function if the input was invalid

    if not puzzle_validity(puzzle):
        messagebox.showinfo("Sudoku Solver", "Invalid puzzle configuration detected. Please check the puzzle and try again.")
        return

    try:
        if solve_sudoku(puzzle):
            display_solution(puzzle)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists for this puzzle.")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred during solving: " + str(e))

def create_grid(app):
    global grid_entries
    grid_entries = []
    for block_row in range(3):
        for block_col in range(3):
            block_frame = tk.Frame(app, background='black', bd=2)
            block_frame.grid(row=block_row, column=block_col, padx=2, pady=2, sticky="nsew")
            for row in range(3):
                for col in range(3):
                    entry_row, entry_col = block_row * 3 + row, block_col * 3 + col
                    entry = tk.Entry(block_frame, width=3, font=("Arial", 24), justify="center")
                    entry.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
                    if len(grid_entries) <= entry_row:
                        grid_entries.append([])
                    grid_entries[entry_row].append(entry)
    solve_button = tk.Button(app, text="Solve", command=solve)
    solve_button.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=2, pady=2)

def show_main_window():
    global app
    app = tk.Tk()
    app.title("Sudoku Solver")
    create_grid(app)
    app.mainloop()

def instructions():
    instruction_window = tk.Toplevel()
    instruction_window.title("Instructions")
    instructions = """Welcome to the Sudoku Solver!\n
    Please enter the numbers of the unsolved Sudoku puzzle into the grid on the next page.
    Use the 'Solve' button to find the solution.
    Leave the cell empty for empty cells in your puzzle.\n
    Thanks for using, and hope you enjoy!"""
    instruction_label = tk.Label(instruction_window, text=instructions, font=("Arial", 14), justify="left")
    instruction_label.pack(padx=10, pady=10)
#button to close instructions window 
    def ok_click():
        instruction_window.destroy()
        show_main_window()

    ok_button = tk.Button(instruction_window, text="Ok", command=ok_click)
    ok_button.pack(pady=20)

def main():
    global app
    app = tk.Tk()
    app.withdraw()  # Initially hide the main window
    instructions()
    app.mainloop()

if __name__ == "__main__":
    main()
