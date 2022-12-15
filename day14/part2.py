import time
import os

# create grid
grid = []

for _ in range(1000):
    grid.append(["."]*1000)

highest_y = 0 # lowest y-level in the graphical representation

# parse input
path = input()

while path != "0":
    path = path.split(" -> ")

    for i in range(len(path)-1):
        x1 = int(path[i].split(",")[0])
        y1 = int(path[i].split(",")[1])
        x2 = int(path[i+1].split(",")[0])
        y2 = int(path[i+1].split(",")[1])

        highest_y = max(highest_y, y1)

        if x1 != x2: 
            start = min(x1, x2)
            end = max(x1, x2)
            
            for j in range(end-start+1):
                grid[y1][start+j] = "#"

        elif y1 != y2: 
            start = min(y1, y2)
            end = max(y1, y2)

            for j in range(end-start+1):
                grid[start+j][x1] = "#"


    path = input()

# add floor to the grid
grid[highest_y+2] = ["#"]*1000

# pretty print grid
def render(grid, x1, x2, y1, y2):
    ystart = min(y1, y2)
    xstart = min(x1, x2)

    for y in range(abs(y1-y2)):
        for x in range(abs(x1-x2)):
            print(grid[ystart+y][xstart+x], end=" ")
        print()

# simulate sand
class Pos: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def get_item(pos):
    return grid[pos.y][pos.x]

def set_item(pos, item):
    grid[pos.y][pos.x] = item

SAND_SRC = Pos(500, 0)
set_item(SAND_SRC, "+")

# returns new sand pos, or False if sand has rested
def tick(sand):
    down = Pos(sand.x, sand.y+1)
    diagonal_left = Pos(sand.x-1, sand.y+1)
    diagonal_right = Pos(sand.x+1, sand.y+1)

    if get_item(down) == ".":
        return down
    elif get_item(diagonal_left) == ".":
        return diagonal_left
    elif get_item(diagonal_right) == ".":
        return diagonal_right
    else: 
        return False

sand_count = 0

while True: 
    new_pos = SAND_SRC

    while new_pos: 
        old_pos = new_pos
        new_pos = tick(old_pos)

        # os.system('cls')
        # render(grid, 493, 504, 0, 10)

    set_item(old_pos, "O")
    sand_count += 1

    if get_item(SAND_SRC) == "O":
        print(sand_count)
        break
    