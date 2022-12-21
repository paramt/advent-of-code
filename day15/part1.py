SIZE = 10*1000*1000
Y_LVL = 2000000

class Pos: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Row: 
    def __init__(self, size):
        self.size = size
        self.row = ["."]*size*2

    def __str__(self): 
        return "".join(self.row)

    def set(self, center, item, spread=0):
        for i in range(spread+1):
            self.row[center+i+(self.size//2)] = item
            self.row[center-i+(self.size//2)] = item


line = input()

row = Row(SIZE)
beacons = []

while line != "0":
    sensor = Pos(int(line.split("=")[1].split(",")[0]), int(line.split("=")[2].split(":")[0]))
    beacon = Pos(int(line.split("=")[3].split(",")[0]), int(line.split("=")[4]))
    beacons.append(beacon)

    d1 = sensor.distance(beacon)
    d2 = abs(Y_LVL - sensor.y)
    
    row.set(sensor.x, "#", d1-d2)

    line = input()

for b in beacons: 
    if b.y == Y_LVL:
        row.set(b.x, "B")

print(row.row.count("#"))