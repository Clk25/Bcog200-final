from pprint import pprint


def next_empty(puzzle):   #locates next empty spot(denoted -1) and returns row,col as a tuple or none if puzzle filled
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == -1:
				return r, c
    return None, None  # if entire puzzle is filled

def is_valid(puzzle,guess,row,col):    
# this function will serve to check wheather a guesss for a given row and col is valid and returns a boolean true/false
# ensures that guess follows conventions of sudoku (so no identical values in same row, col or 3x3 box) 
def solve_sudoku(puzzle):
#this will be the function that actually solves/generates a solution to the given puzzle and will cosntitute most of the coding
#puzzle represented as list with sublists corresponding to each row
#If solution was found to exist than list will be mutated to replace all empty spaces with valid answers
#first this function will find a space with a negative one 
#Then it will make a guess (so 1-9), then the next step will be to check if this is a valid guess
#if valid we will place this guess on that row/col location in the list