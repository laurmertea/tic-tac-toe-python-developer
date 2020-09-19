# Description
# It is time to learn to see the result (or lack thereof) of the game. 
# In this stage, you should analyze a Tic-Tac-Toe field.
# Is it already clear who's the winner or is the game not over yet? 
# Is it a draw or an impossible combination of moves? Let's find out!
# Note, in this stage either 'X' or 'O' can start the game.
#
# Objectives
# In this stage your program should:
# Fill the field from the input and print it as in the previous stage.
# Find the state in which the game is at the moment and print it. 
# Possible states:
# "Game not finished" when no side has a three in a row but there are still empty cells;
# "Draw" when no side has a three in a row and there are no empty cells left;
# "X wins" when the field has three Xs in a row;
# "O wins" when the field has three Os in a row;
# "Impossible" when the field has three Xs in a row as well as three Os in a row. 
# Or the field has a lot more Xs that Os or vice versa (if the difference is 2 or more, should be 1 or 0). 
# For this stage, consider that the game can start both with X or O.
# Also, you can use ' ' or '_' to print empty cells - it's up to you.
#
# Examples
# The examples below show outputs for some predefined states. Your program should work in the same way.
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that these are not part of the input.
#
# Example 1:
# Enter cells: > XXXOO__O_
# ---------
# | X X X |
# | O O _ |
# | _ O _ |
# ---------
# X wins
#
# Example 2:
#
# Enter cells: > XOXOXOXXO
# ---------
# | X O X |
# | O X O |
# | X X O |
# ---------
# X wins
# Example 3:
#
# Enter cells: > XOOOXOXXO
# ---------
# | X O O |
# | O X O |
# | X X O |
# ---------
# O wins
# Example 4:
#
# Enter cells: > XOXOOXXXO
# ---------
# | X O X |
# | O O X |
# | X X O |
# ---------
# Draw
# Example 5:
#
# Enter cells: > XO_OOX_X_
# ---------
# | X O   |
# | O O X |
# |   X   |
# ---------
# Game not finished
# Example 6:
#
# Enter cells: > XO_XO_XOX
# ---------
# | X O _ |
# | X O _ |
# | X O X |
# ---------
# Impossible
# Example 7:
#
# Enter cells: > _O_X__X_X
# ---------
# |   O   |
# | X     |
# | X   X |
# ---------
# Impossible
# Example 8:
#
# Enter cells: > _OOOO_X_X
# ---------
# |   O O |
# | O O   |
# | X   X |
# ---------
# Impossible

def setup(symbols, old = " ", new = "_"):
    return symbols.replace(old, new)

def margins(pattern = None):
    if pattern is None:
        return "---------"
    return pattern

def line(part, separator = " ", wall = "|"):
    line = wall + separator
    for elem in part:
        line += elem + separator
    return line + wall

def get_parts(symbols, size):
    return [symbols[i:i+size] for i in range(0, len(symbols), size)]

def result_on_line(parts, size = 3):
    result = []
    winner = False
    for line in parts:
        for symbol in line:
            line_result = False
            if symbol == "X" or symbol == "O":
                if line.count(symbol) == size:
                    line_result = symbol
                    winner = symbol
        result.append(line_result)

    if result.count(False) < size - 1:
        return -1
    if not any(result):
        return 0
    return winner

def result_on_column(parts, size = 3):
    result = []
    winner = False
    for part_index in range(0, size):
        column_result = True
        symbol = False
        for column_index in range(0, size):
            if column_index > 0:
                column_result = column_result == (parts[column_index][part_index] == parts[column_index - 1][part_index]) == True
                if parts[column_index][part_index] != "_":
                    symbol = parts[column_index][part_index]
        if column_result == True and symbol:
            result.append(symbol)
            winner = symbol
        else:
            result.append(False)
    if result.count(False) < size - 1:
        return -1
    if not any(result):
        return 0
    return winner

def result_on_diagonal(parts, size = 3):
    result = []
    winner = False
    diagonal_result = True
    for index in range(0, size):
        if index > 0:
            diagonal_result = diagonal_result == (parts[index][index] == parts[index - 1][index - 1]) == True
            if parts[index][index] != "_":
                symbol = parts[index][index]
    if diagonal_result == True:
        result.append(symbol)
        winner = symbol
    else:
        result.append(False)

    diagonal_result = True
    reverse = size - 1
    for index in range(0, size):
        if index > 0:
            diagonal_result = diagonal_result == (parts[reverse][index] == parts[reverse + 1][index - 1]) == True
            if parts[reverse][index] != "_":
                symbol = parts[reverse][index]
        reverse -= 1
    if diagonal_result == True:
        result.append(symbol)
        winner = symbol
    else:
        result.append(False)
    
    if result.count(False) == 0:
        return -1
    if winner:
        return winner
    return 0

def is_impossible(symbols):
    return abs(symbols.count("X") - symbols.count("O")) >= 2 

def is_filled(symbols, empty = "_"):
    return symbols.count(empty)

def analyze(symbols, size = 3):
    if is_impossible(symbols):
        return "Impossible"

    parts = get_parts(symbols, size)
    line_results = result_on_line(parts)
    column_results = result_on_column(parts)
    diagonal_results = result_on_diagonal(parts)

    if (type(line_results) is str and type(column_results) is str) or (type(line_results) is str and type(diagonal_results) is str) or (type(column_results) is str and type(diagonal_results) is str):
        return "Impossible"

    if line_results == -1:
        return "Impossible"
    elif line_results != 0:
        return line_results + " wins"
    
    if column_results == -1:
        return "Impossible"
    elif column_results != 0:
        return column_results + " wins"

    if diagonal_results == -1:
        return "Impossible"
    elif diagonal_results != 0:
        return diagonal_results + " wins"

    if is_filled(symbols) == 0:
        return "Draw"
    else:
        return "Game not finished"

def battlefield(symbols, size = 3, inline = None):
    if inline is not True:
        ending = "\n"
    battlefield = margins() + ending
    symbols = setup(symbols)
    parts = get_parts(symbols, size)
    for part in parts:
        battlefield += line(part) + ending
    battlefield += margins()
    
    print(battlefield)
    print(analyze(symbols))

cells = input("Enter cells: \n")
battlefield(cells)