import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)

def debug_maze(maze):
    message = ""
    for i in maze:
        for j in i:
            message += j
        message += "\n"
    print(message[:-1], file=sys.stderr, flush=True)

def print_maze(maze):
    message = ""
    for i in maze:
        for j in i:
            message += j
        message += "\n"
    print(message[:-1])


def find_non_wall_direction(maze, row, col, lines, width):
    if maze[row][col] == "S":
        return [(row, col, row, col)]
    directions = []
    for new_r, new_c in [
        (row-1, col),
        (row, col-1), 
        (row+1, col), 
        (row, col+1), 
        ]:
        if is_special_position(new_r, new_c, lines, width):
            new_r, new_c = correct_position(new_r, new_c, lines, width)
        if maze[new_r][new_c] == ".":
            directions.append((new_r, new_c, row, col))
            debug(f"{row}, {col} row, col")
    return directions

def correct_position(row, col, lines, cols):
    debug(f"{row} {col}", "old")
    if col == cols:
        col = 0
    elif col < 0:
        col = cols-1
    if row == lines:
        row = 0
    elif row <0:
        row = lines -1
    debug(f"{row} {col}", "new")
    return row, col

def correct_old_position(row, col, lines, cols):
    debug(f"{row} {col}", "old")
    if col == cols:
        col = 0
    elif col < 0:
        col = cols-1
    if row == lines:
        row = 0
    elif row <0:
        row = lines -1
    debug(f"{row} {col}", "new")
    return row, col
def is_special_position(row, col, lines, cols):
    debug(f"{row} {col}{width} {height}", "is_special_position")
    if col == cols:
        return True
    if col == -1:
        return True
    if row == lines:
        return True
    if row == -1:
        return True
    debug("not special")
    return False


def set_actual_row(maze, row, column, index, width):
    debug(index, "indexxxx")
    maze[row][column] = index
    debug("\n")
    debug_maze(maze)


indexes = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def get_index(row, column, maze):
    debug(f"{row} {column}", "in_get_index")
    return indexes.index(maze[row][column])

start_row, start_column = 0,0
width, height = [int(i) for i in input().split()]
maze = []
for i in range(height):
    row = input()
    debug(row)
    maze.append([i for i in row])
    if "S" in row:
        start_column = row.index("S")
        start_row = i



debug(f"{width} {height}", "wh")
# debug_maze(maze)
debug(start_row, "start_row")
debug(start_column, "start_column")
index = 0
directions = []
while True:
    if index == 0:
        set_actual_row(maze, start_row, start_column, "0", width)
        index += 1
        continue
    actual_directions = find_non_wall_direction(maze, start_row, start_column, height, width)
    directions.extend(actual_directions)
    debug(directions, "directions 1")
    if not directions:
        break
    start_row, start_column, old_row, old_column = directions[0]
    directions.remove((start_row, start_column, old_row, old_column))
    debug(directions, "directions 2")
    old_number = get_index(old_row, old_column, maze)
    debug(old_number, "old_number")
    debug(directions, "directions 2")

    debug(directions, "directions")

    set_actual_row(maze, start_row, start_column, str(indexes[old_number+1]), width)
    index += 1
    debug(start_row, "start_row")
    debug(start_column, "start_column")
# for line in maze:
# for i in range(height):

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

print_maze(maze)
