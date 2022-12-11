from time import time

line = input()
trees = []
count = 0

while line != "0":
    trees.append(list(map(int, list(line))))
    line = input()

start = time()

def seen(line, tree):
    return len(line) == 0 or max(line) < tree

for y, row in enumerate(trees):
    for x, tree in enumerate(row):

        if x == 0 or y == 0 or x == len(trees)-1 or y == len(row)-1:
            count += 1
        else:
            left = row[:x]
            right = row[x+1:]

            vertical = [tree[x] for tree in trees]
            top = vertical[:y]
            bottom = vertical[y+1:]

            if seen(left, tree) or seen(right, tree) or seen(top, tree) or seen(bottom, tree):
                count += 1


print(time() - start)
print(count)