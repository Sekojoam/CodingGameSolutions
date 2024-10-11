import sys
import math

hasFindControl = [False]
def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
rows, columns, roundsNumberForAlarm = [int(i) for i in input().split()]
def has_find_control(labyrinthe, rickRow, rickColumn):
    char = labyrinthe[rickRow][rickColumn]
    if char == "C":
        hasFindControl[0] = True
    debug(hasFindControl, "hasFindControl")
    
# game loop
rickPath = []
rickDirections = []
debug(roundsNumberForAlarm, "roundsNumberForAlarm")

def get_opposite_direction(direction):
    if direction == "UP":
        return "DOWN"
    elif direction == "DOWN":
        return "UP"
    elif direction == "LEFT":
        return "RIGHT"
    else:
        return "LEFT"

def find_coordinates_for_direction(direction, labyrinthe, rickRow, rickColumn):
    if direction == "UP":
        nextRow = rickRow-1
        nextColumn = rickColumn
    elif direction == "DOWN":
        nextRow = rickRow+1
        nextColumn = rickColumn
    elif direction == "LEFT":
        nextRow = rickRow
        nextColumn = rickColumn-1
    else:
        nextRow = rickRow
        nextColumn = rickColumn+1
    return nextRow, nextColumn

def is_coordinates_a_wall(labyrinthe, nextRow, nextColumn):
    char = labyrinthe[nextRow][nextColumn]
    if char == "#":
        return True
    return False

def was_direction_in_my_path(nextRow, nextColumn):
    if (nextRow, nextColumn) in rickPath:
        return True
    return False

def find_control_direction(labyrinthe, rickRow, rickColumn, previousDirection):
    for direction in [previousDirection, "UP", "DOWN", "LEFT", "RIGHT"]:
        if direction == "":
            continue
        nextRow, nextColumn = find_coordinates_for_direction(direction, labyrinthe, rickRow, rickColumn)
        wasDirectionInMyPath = was_direction_in_my_path(nextRow, nextColumn)
        debug(direction, "find_control_direction")
        debug(wasDirectionInMyPath, "wasDirectionInMyPath")
        if wasDirectionInMyPath:
            continue
        isCoordinatesAWall = is_coordinates_a_wall(labyrinthe, nextRow, nextColumn)
        debug(isCoordinatesAWall, "isCoordinatesAWall")
        if not isCoordinatesAWall:
            return direction


previousDirection= ""
while True:
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    rickRow, rickColumn = [int(i) for i in input().split()]
    rickPath.append((rickRow, rickColumn))
    labyrinthe = []
    for i in range(rows):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        labyrinthe.append(row)
    debug("\n".join(labyrinthe))
    debug(rickPath, "rickPath")
    has_find_control(labyrinthe, rickRow, rickColumn)

    if not hasFindControl[0]:
        direction = find_control_direction(labyrinthe, rickRow, rickColumn, previousDirection)
        previousDirection = direction
        print(direction)
        rickDirections.append(direction)
    else:
        direction = get_opposite_direction(rickDirections.pop())
        print(direction)

    if len(rickPath)>roundsNumberForAlarm*3:
        break
