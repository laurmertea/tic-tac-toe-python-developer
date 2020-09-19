# Description
# In addition to analyzing the field, it is equally important to add the ability to select a cell for your move. 
# Now you need to implement players' moves. Let's divide the field into cells.
# Suppose the bottom left cell has the coordinates (1, 1) 
# and the top right cell has the coordinates (3, 3) like in this table:
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
# The program should ask to enter the coordinates where a user wants to make a move.
# Note that in this stage user places X, not O. 
# Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. 
# Also, notice that coordinates start with 1 and can be 1, 2, or 3.
# What if the user enters incorrect coordinates? 
# The user could enter symbols instead of numbers or enter coordinates of the already occupied cells. 
# You need to prevent all of that by checking user's input and catching possible exceptions.
#
# Objectives
# The program should work in the following way:
# Get the 3x3 field from the input as in the previous stages.
# Output this 3x3 field with cells before the user's move.
# Then ask the user about his next move.
# Then the user should input 2 numbers that represent the coordinates of the cell which they want to mark X or O. 
# (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input)
# Analyze user input and show these messages in the following situations:
# -"This cell is occupied! Choose another one!" if the cell is not empty;
# -"You should enter numbers!" if the user enters other symbols instead of numbers;
# -"Coordinates should be from 1 to 3!" if the user goes beyond the field.
# Then output the table including the user's most recent move.
# The program should also check user input. If it's unsuitable, the program should ask them to enter their coordinates once again.
# So, you need to output a field from the first line of the input and then ask the user to make their move. 
# Keep asking until the user enters coordinates that represent an empty cell on the field 
# and after that output the field with that move. You should output the field only 2 times, before and after a correct move.
# Do not delete code that checks table state; it will be useful in the future.
#
# Examples
# The examples below show how your program should work.
# The greater-than symbol followed by space (> ) represent user input. 
# Notice that these are not part of the input.
#
# Example 1:
# Enter cells: > X_X_O____
# ---------
# | X   X |
# |   O   |
# |       |
# ---------
# Enter the coordinates: > 1 1
# ---------
# | X   X |
# |   O   |
# | X     |
# ---------
#
# Example 2:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > 1 3
# ---------
# | X X X |
# | O O   |
# | O X   |
# ---------
#
# Example 3:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > 3 1
# ---------
# |   X X |
# | O O   |
# | O X X |
# ---------
#
# Example 4:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > 3 2
# ---------
# |   X X |
# | O O X |
# | O X   |
# ---------
#
# Example 5:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > 1 1
# This cell is occupied! Choose another one!
# Enter the coordinates: > 1 3
# ---------
# | X X X |
# | O O   |
# | O X   |
# ---------
#
# Example 6:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > one
# You should enter numbers!
# Enter the coordinates: > one three
# You should enter numbers!
# Enter the coordinates: > 1 3
# ---------
# | X X X |
# | O O   |
# | O X   |
# ---------
#
# Example 7:
# Enter cells: > _XXOO_OX_
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# Enter the coordinates: > 4 1
# Coordinates should be from 1 to 3!
# Enter the coordinates: > 1 4
# Coordinates should be from 1 to 3!
# Enter the coordinates: > 1 3
# ---------
# | X X X |
# | O O   |
# | O X   |
# ---------

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

def valid(coordinate):
    if coordinate.isnumeric() is False:
        print("You should enter numbers!")
        return False

    if int(coordinate) > 3 or int(coordinate) < 1:
        print("Coordinates should be from 1 to 3!")
        return False

    return True

def move(symbols, size = 3):
    move = False
    
    while move is False:
        y, x = input("Enter the coordinates: \n").split()
        move = valid(x) and valid(y)

        if move:
            parts = get_parts(symbols, size)
            
            if parts[3 - int(x)][int(y) - 1] != "_":
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
    symbols = setup(symbols)
    parts = get_parts(symbols, size)
    for part in parts:
        battlefield += line(part) + ending
    battlefield += margins()
    
    print(battlefield)
    # print(analyze(symbols))

cells = input("Enter cells: \n")
battlefield(cells)
battlefield(move(cells))