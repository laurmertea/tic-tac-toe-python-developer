# Description
# We are at the finish line! But playing alone is not so interesting, is it? Let's combine our successes in past stages 
# and get Tic-Tac-Toe with the ability to play from the beginning (empty field) to the result (win or draw).
# Now it is time to make a working game!
# In the last stage, make it so you can play a full game with a friend. First one of you moves as X, 
# and then the other one moves as O.
# 
# Objectives
# In this stage, you should write a program that:
# Prints an empty field at the beginning of the game.
# Creates a game loop where the program asks the user to enter the cell coordinates, 
# analyzes the move for correctness and shows a field with the changes if everything is ok.
# Ends the game when someone wins or there is a draw.
# You need to output the final result after the end of the game.
# Good luck gaming!
# 
# Example
# The example below shows how your program should work.
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.
# 
# ---------
# |       |
# |       |
# |       |
# ---------
# Enter the coordinates: > 2 2
# ---------
# |       |
# |   X   |
# |       |
# ---------
# Enter the coordinates: > 2 2
# This cell is occupied! Choose another one!
# Enter the coordinates: > two two
# You should enter numbers!
# Enter the coordinates: > 1 4
# Coordinates should be from 1 to 3!
# Enter the coordinates: > 1 3
# ---------
# | O     |
# |   X   |
# |       |
# ---------
# Enter the coordinates: > 3 1
# ---------
# | O     |
# |   X   |
# |     X |
# ---------
# Enter the coordinates: > 1 2
# ---------
# | O     |
# | O X   |
# |     X |
# ---------
# Enter the coordinates: > 1 1
# ---------
# | O     |
# | O X   |
# | X   X |
# ---------
# Enter the coordinates: > 3 2
# ---------
# | O     |
# | O X O |
# | X   X |
# ---------
# Enter the coordinates: > 2 1
# ---------
# | O     |
# | O X O |
# | X X X |
# ---------
# X wins


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

def empty_field(size = 3, empty_cell = " "):
    return (empty_cell * size) * size

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

def result_on_column(parts, size = 3, empty_field = " "):
    result = []
    winner = False
    for part_index in range(0, size):
        column_result = True
        symbol = False
        for column_index in range(0, size):
            if column_index > 0:
                column_result = column_result == (parts[column_index][part_index] == parts[column_index - 1][part_index]) == True
                if parts[column_index][part_index] != empty_field:
                    symbol = parts[column_index][part_index]
        if column_result == True and symbol != empty_field:
            result.append(symbol)
            winner = symbol
        else:
            result.append(False)
    if result.count(False) < size - 1:
        return -1
    if not any(result):
        return 0
    return winner

def result_on_diagonal(parts, size = 3, empty_field = " "):
    result = []
    winner = False
    diagonal_result = True
    symbol = empty_field

    for index in range(0, size):
        if index > 0:
            diagonal_result = diagonal_result == (parts[index][index] == parts[index - 1][index - 1] != empty_field) == True
            if parts[index][index] != empty_field:
                symbol = parts[index][index]
    
    if diagonal_result == True and symbol != empty_field:
        result.append(symbol)
        winner = symbol
    else:
        result.append(False)

    diagonal_result = True
    reverse = size - 1

    for index in range(0, size):
        if index > 0:
            diagonal_result = diagonal_result == (parts[reverse][index] == parts[reverse + 1][index - 1] != empty_field) == True
            if parts[reverse][index] != empty_field:
                symbol = parts[reverse][index]
        reverse -= 1
    if diagonal_result == True and symbol != empty_field:
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

def is_filled(symbols, empty_field = " "):
    return symbols.count(empty_field)

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

def valid(coordinate):
    if coordinate.isnumeric() is False:
        print("You should enter numbers!")
        return False

    if int(coordinate) > 3 or int(coordinate) < 1:
        print("Coordinates should be from 1 to 3!")
        return False

    return True

def move(symbols, size = 3, empty_field = " "):
    move = False
    
    while move is False:
        y, x = input("Enter the coordinates: \n").split()
        move = valid(x) and valid(y)

        if move:
            parts = get_parts(symbols, size)
            
            if parts[3 - int(x)][int(y) - 1] != empty_field:
                print("This cell is occupied! Choose another one!")
                move = False
            else:
                if symbols.count("X") > symbols.count("O"):
                    mark = "O"
                else:
                    mark = "X"

                line_list = list(parts[3 - int(x)])
                line_list[int(y) - 1] = mark
                parts[3 -int(x)] = "".join(line_list)

    return "".join(parts)

def battlefield(symbols, size = 3, inline = None):
    if inline is not True:
        ending = "\n"
    
    battlefield = margins() + ending
    parts = get_parts(symbols, size)

    for part in parts:
        battlefield += line(part) + ending
    battlefield += margins()
    
    print(battlefield)

def tic_tac_toe(size = 3):
    symbols = empty_field(size)
    battlefield(symbols)
    result = ""

    while result != "finished":
        symbols = move(symbols)
        battlefield(symbols)
        status = analyze(symbols)

        if (status != "Game not finished"):
            print(status)
            result = "finished"

tic_tac_toe()