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

indexes = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
class Node:

    def __init__(self, row, col, previous):
        self.row = row
        self.col = col
        self.previous : Node = previous
        self.branches : list[Node] = []
        self.number = 0

    def write_in_maze(self, maze, number=None):
        if number == 0:
            text = "0"
        else:
            self.number = self.previous.number + 1
            text = indexes[self.number]
        
        maze[self.row][self.col] = text
        debug("\n")
        debug_maze(maze)
    
    def find_branches(self, maze):
        for new_r, new_c in [
            (self.row, self.col-1), 
            (self.row, self.col+1), 
            (self.row+1, self.col), 
            (self.row-1, self.col),
            ]:
            lines = len(maze)
            cols = len(maze[0])
            if is_special_position(new_r, new_c, lines, cols):
                new_r, new_c = correct_position(new_r, new_c, lines, cols)
            if maze[new_r][new_c] == ".":
                self.branches.append(Node(new_r, new_c, self))
        return self.branches

    def str_version(self):
        return f"{self.row}-{self.col}"


class Graph:

    def __init__(self):
        self.vertices : list[Node] = []
        self.queue : list[Node] = []
        self.order : list[str] = []

    def bfs(self, first_row, first_column, maze):
        node = Node(first_row, first_column, None)
        self.vertices.append(node)
        self.order.append(node.str_version())
        node.write_in_maze(maze, 0)
        branches = node.find_branches(maze)
        self.queue.extend(branches)
        bfsIndex = 0
        for node in self.queue:
            if node.str_version() in self.order:
                debug(self.order)
                debug(node.str_version())
                continue
            self.vertices.append(node)
            self.order.append(node.str_version())
            node.write_in_maze(maze)
            node.find_branches(maze)
            self.queue.extend(node.branches)
            bfsIndex += 1
        debug(f"solution found in {bfsIndex} rounds")

def print_maze(maze):
    message = ""
    for i in maze:
        for j in i:
            message += j
        message += "\n"
    print(message[:-1])


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

def is_special_position(row, col, lines, cols):
    if col == cols:
        return True
    if col == -1:
        return True
    if row == lines:
        return True
    if row == -1:
        return True
    return False

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
debug(start_row, "start_row")
debug(start_column, "start_column")

graph = Graph()
graph.bfs(start_row, start_column, maze)
print_maze(maze)
