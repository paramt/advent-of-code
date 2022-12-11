line = input()
cycle = 0
X = 1
display = ""

def draw():
    global display

    if (cycle)%40 == X or (cycle)%40 == X-1 or (cycle)%40 == X+1:
        display += "#"
    else:
        display += " "

while line != "0":
    if line == "noop":
        draw()
        cycle += 1
    else: 
        draw()
        cycle += 1
        draw()
        cycle += 1

        X += int(line.split(" ")[1])


    line = input()


print()
for i in range(6):
    print(display[40*i:40*(i+1)])

