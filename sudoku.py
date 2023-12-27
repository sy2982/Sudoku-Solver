#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this

    empty = isEmpty(board)

    # Check for blank spaces
    if not empty:
        return board
    else:
        position = empty

    # Minimum remaining value heuristic
    values = csp(board, position)

    for value in values:
        # Foward checking constraints for backtracking
        if constraints(board, position, value):
            board[position] = value
            solved = backtracking(board)

            if solved is not None:
                return solved                 
            board[position] = 0

    return None
    
def isEmpty(board):
    # Check for 0's and return key/position
    for key, assignment in board.items():
            if assignment == 0:
                return key
    return None

def constraints(board, position, assignment):
    # Position(r,c)
    row = position[0]
    col = position[1]

    # Set constraints for row, column, box assignments
    for r in ROW:
        if board[f"{r}{col}"] == assignment and r!= row:
            return False

    for c in COL:
        if board[f"{row}{c}"] == assignment and c!= col:
            return False
        
    row_start, col_start = int((ord(row) - 65) // 3), int((int(col) - 1) // 3)
    for i in range(row_start * 3, row_start * 3 + 3):
        for j in range(col_start * 3, col_start * 3 + 3):
            if board[ROW[i] + COL[j]] == assignment and (ROW[i], COL[j]) != position:
                return False
    
    # Return true if value follows constraints
    return True

def csp(board, position):
    # Position(r,c)
    row = position[0]
    col = position[1]

    # Domain values
    row_domain = set()
    col_domain = set()
    box_domain = set()

    # Get row, column, and box domain values 
    for c in COL:
        if board[f"{row}{c}"] != 0:
            row_domain.add(board[f"{row}{c}"])

    for r in ROW:
        if board[f"{r}{col}"] != 0:
            col_domain.add(board[f"{r}{col}"])

    row_start, col_start = 3 * (int((ord(row) - 65) // 3)), 3 * (int((int(col) - 1) // 3))
    for i in range(3):
        for j in range(3):
            cell_value = board[f"{ROW[row_start + i]}{COL[col_start + j]}"]
            if cell_value != 0:
                box_domain.add(cell_value)

    # Get values not in domains
    remaining_values = {num for num in range(1, 10)} - row_domain - col_domain - box_domain
    remaining_values = list(remaining_values)

    return remaining_values

if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        board = backtracking(board)

        print(board_to_string(board))
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        
        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(board)

            # Write board to file
            outfile.write(board_to_string(board))
            outfile.write('\n')

        print("Finishing all boards in file.")