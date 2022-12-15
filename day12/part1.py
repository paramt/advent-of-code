# Set start and end
START = {"x": 0, "y": 20}
END = {"x": 119, "y": 20}

grid = []
line = input()

while line != "0":
    grid.append(list(line.replace("S", "a").replace("E", "z")))
    line = input()

def possible_steps(pos):
    elevation = ord(grid[pos["y"]][pos["x"]])

    steps = []

    if pos["y"] < len(grid)-1 and ord(grid[pos["y"]+1][pos["x"]]) <= elevation + 1:
        steps.append({"x": pos["x"], "y": pos["y"]+1})
    if pos["y"] >= 1 and ord(grid[pos["y"]-1][pos["x"]]) <= elevation + 1:
        steps.append({"x": pos["x"], "y": pos["y"]-1})
    if pos["x"] < len(grid[0])-1 and ord(grid[pos["y"]][pos["x"]+1]) <= elevation + 1:
        steps.append({"x": pos["x"]+1, "y": pos["y"]})
    if pos["x"] >= 1 and ord(grid[pos["y"]][pos["x"]-1]) <= elevation + 1:
        steps.append({"x": pos["x"]-1, "y": pos["y"]})

    return steps

visited = [[START, 0]]
queue = [[START, 0]]

while queue: 
    node, depth = queue.pop(0)

    if node == END: 
        print("done!")
        print(depth)

    for n in possible_steps(node):
        if n not in [visited_node[0] for visited_node in visited]: 
            visited.append([n, depth+1])
            queue.append([n, depth+1])

