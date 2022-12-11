line = input()
trees = []
count = 0

while line != "0":
    trees.append(list(map(int, list(line))))
    line = input()

def seen(line, tree):
    if line == None or len(line) == 0: return 0
    for i, t in enumerate(line):
        if t >= tree: 
            return i+1
    
    return len(line)

for y, row in enumerate(trees):
    for x, tree in enumerate(row):

        hidden = False

        left = list(reversed(trees[y][:x]))
        right = trees[y][x+1:]

        vertical = []

        for row in trees:
            vertical.append(row[x])

        top = list(reversed(vertical[:y]))
        bottom = vertical[y+1:]

        count = max(count, seen(left, tree) * seen(right, tree) * seen(top, tree) * seen(bottom, tree))



print(count)
            

            
        
# print(count)
#print(seen([1, 2, 3, 4, 5], 5))