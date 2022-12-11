line = input()
cycle = 1
X = 1
total = 0

def add_signal_strength():
    global total 
    if (cycle + 20) % 40 == 00: 
        total += X * cycle

while line != "0":
    if line == "noop":
        add_signal_strength()
        cycle += 1
    else: 
        add_signal_strength()
        cycle += 1
        add_signal_strength()
        cycle += 1

        X += int(line.split(" ")[1])


    line = input()


print(total)