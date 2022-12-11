from collections import defaultdict
from functools import reduce
from time import time



line = input()
trees = []

while line != "0":
    trees.append(list(map(int, list(line))))
    line = input()

start = time()

visible = [[0] * len(trees[0]) for _ in range(len(trees))]

# left
for y, row in enumerate(trees):
    highest = -1

    for x, tree in enumerate(row):
        if tree > highest: visible[y][x] = 1
        highest = max(highest, tree)

# right
for y, row in enumerate(trees):
    highest = -1

    for x in range(len(row)-1, 0, -1):
        if row[x] > highest: visible[y][x] = 1
        highest = max(highest, row[x])

# top
for x in range(len(trees[0])):
    highest = -1

    for y in range(len(trees)):
        if trees[y][x] > highest: 
            visible[y][x] = 1
        highest = max(highest, trees[y][x])

# bottom
for x in range(len(trees[0])):
    highest = -1

    for y in range(len(trees)-1, 0, -1):
        if trees[y][x] > highest: visible[y][x] = 1
        highest = max(highest, trees[y][x])



total = 0
for y, row in enumerate(visible):
    # for x, i in enumerate(row): 
    #     if i == 0: print(f"x: {x}, y: {y}")

    total += row.count(1)

print(time() - start)

print(total)

# for row in visible:
#     print(row)

# reduce(lambda x, y: x.count(1) + y, trees)
